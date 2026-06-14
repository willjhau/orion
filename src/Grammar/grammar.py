"""
Orion language parser — tokenizer + recursive descent.

Replaces the original depth-first search grammar walker with an O(n)
tokenizer followed by an O(n) recursive-descent parse.  The output is
the same SyntaxTreeNode tree that the interpreter consumes (equivalent
to the post-tidyTree structure produced by the old parser).
"""

from ..Structures.syntaxTree import SyntaxTreeNode


# ─── Symbol / node helpers ────────────────────────────────────────────────────

class Symbol:
    """Thin wrapper kept for backward compatibility with any code that
    inspects node.symbol.name / node.symbol.terminal."""

    __slots__ = ('name', 'terminal')

    def __init__(self, name, terminal=False):
        self.name = name
        self.terminal = terminal

    def __repr__(self):
        return self.name


def _sym(name, terminal=False):
    return Symbol(name, terminal)


def _node(name, matched, children=None, terminal=False):
    """Create a SyntaxTreeNode with the given symbol name and matched string."""
    n = SyntaxTreeNode(_sym(name, terminal), matched)
    if children:
        for c in children:
            n.add_child(c)
    return n


def _terminal(ch):
    """Create a single-character terminal node."""
    return _node(ch, ch, terminal=True)


# ─── Tokenizer ────────────────────────────────────────────────────────────────

class TT:  # TokenType constants
    INT_KW    = 'int'
    FLOAT_KW  = 'float'
    BOOLEAN_KW = 'boolean'
    CHAR_KW   = 'char'
    STRING_KW = 'String'
    ARRAY_KW  = 'Array'
    TRUE      = 'true'
    FALSE     = 'false'
    PASS      = 'pass'
    INT_LIT   = 'INT_LIT'
    FLOAT_LIT = 'FLOAT_LIT'
    STRING_LIT = 'STRING_LIT'
    CHAR_LIT  = 'CHAR_LIT'
    IDENT     = 'IDENT'
    PLUS      = '+'
    MINUS     = '-'
    STAR      = '*'
    SLASH     = '/'
    EQ        = '=='
    NEQ       = '!='
    LTE       = '<='
    GTE       = '>='
    LT        = '<'
    GT        = '>'
    ASSIGN    = '='
    LPAREN    = '('
    RPAREN    = ')'
    LBRACKET  = '['
    RBRACKET  = ']'
    COLON     = ':'
    SEMICOLON = ';'
    COMMA     = ','
    EOF       = 'EOF'


_KEYWORDS = {
    'int':     TT.INT_KW,
    'float':   TT.FLOAT_KW,
    'boolean': TT.BOOLEAN_KW,
    'char':    TT.CHAR_KW,
    'String':  TT.STRING_KW,
    'Array':   TT.ARRAY_KW,
    'true':    TT.TRUE,
    'false':   TT.FALSE,
    'pass':    TT.PASS,
}

_TYPE_KWS = {TT.INT_KW, TT.FLOAT_KW, TT.BOOLEAN_KW,
             TT.CHAR_KW, TT.STRING_KW, TT.ARRAY_KW}

_REL_OPS = {TT.EQ, TT.NEQ, TT.LT, TT.GT, TT.LTE, TT.GTE}

_SINGLE = {
    '+': TT.PLUS,  '-': TT.MINUS, '*': TT.STAR,  '/': TT.SLASH,
    '<': TT.LT,    '>': TT.GT,    '=': TT.ASSIGN,
    '(': TT.LPAREN, ')': TT.RPAREN,
    '[': TT.LBRACKET, ']': TT.RBRACKET,
    ':': TT.COLON, ';': TT.SEMICOLON, ',': TT.COMMA,
}


class Token:
    __slots__ = ('type', 'value')

    def __init__(self, t, v):
        self.type = t
        self.value = v

    def __repr__(self):
        return f'Token({self.type!r}, {self.value!r})'


_EOF_TOKEN = Token(TT.EOF, '')


def tokenize(line: str):
    """Convert a preprocessed source line into a list of Token objects."""
    tokens = []
    i = 0
    n = len(line)
    while i < n:
        c = line[i]

        if c == ' ':
            i += 1
            continue

        # String literal  "..."
        if c == '"':
            j = i + 1
            while j < n and line[j] != '"':
                j += 1
            if j >= n:
                raise SyntaxError("Unterminated string literal")
            tokens.append(Token(TT.STRING_LIT, line[i:j + 1]))
            i = j + 1
            continue

        # Character literal  '.'
        if c == "'":
            if i + 2 < n and line[i + 2] == "'":
                tokens.append(Token(TT.CHAR_LIT, line[i:i + 3]))
                i += 3
                continue
            raise SyntaxError(f"Invalid character literal at position {i}")

        # Numeric literal (int or float)
        if c.isdigit():
            j = i
            while j < n and line[j].isdigit():
                j += 1
            if j < n and line[j] == '.' and j + 1 < n and line[j + 1].isdigit():
                k = j + 1
                while k < n and line[k].isdigit():
                    k += 1
                tokens.append(Token(TT.FLOAT_LIT, line[i:k]))
                i = k
            else:
                tokens.append(Token(TT.INT_LIT, line[i:j]))
                i = j
            continue

        # Identifier or keyword
        if c.isalpha() or c == '_':
            j = i
            while j < n and (line[j].isalnum() or line[j] == '_'):
                j += 1
            word = line[i:j]
            tokens.append(Token(_KEYWORDS.get(word, TT.IDENT), word))
            i = j
            continue

        # Two-character operators
        two = line[i:i + 2]
        if two == '==':
            tokens.append(Token(TT.EQ,  '==')); i += 2; continue
        if two == '!=':
            tokens.append(Token(TT.NEQ, '!=')); i += 2; continue
        if two == '<=':
            tokens.append(Token(TT.LTE, '<=')); i += 2; continue
        if two == '>=':
            tokens.append(Token(TT.GTE, '>=')); i += 2; continue

        # Single-character operators and punctuation
        if c in _SINGLE:
            tokens.append(Token(_SINGLE[c], c))
            i += 1
            continue

        raise SyntaxError(f"Unknown character {c!r} at position {i} in: {line!r}")

    tokens.append(_EOF_TOKEN)
    return tokens


# ─── Recursive descent parser ─────────────────────────────────────────────────

class _Parser:
    def __init__(self, tokens):
        self._t = tokens
        self._pos = 0

    # ── Lookahead helpers ─────────────────────────────────────────

    def _peek(self, offset=0):
        idx = self._pos + offset
        return self._t[idx] if idx < len(self._t) else _EOF_TOKEN

    def _consume(self, expected=None):
        tok = self._t[self._pos]
        if expected is not None and tok.type != expected:
            raise SyntaxError(
                f"Expected {expected!r} but got {tok!r} (pos {self._pos})")
        self._pos += 1
        return tok

    # ── Statement ─────────────────────────────────────────────────

    def parse_statement(self):
        tok = self._peek()

        # pass;
        if tok.type == TT.PASS:
            self._consume()
            self._consume(TT.SEMICOLON)
            return _node('Statement', 'pass;', [_node('pass', 'pass;')])

        # Declaration  (type keyword starts it)
        if tok.type in _TYPE_KWS:
            decl = self._parse_declaration()
            self._consume(TT.SEMICOLON)
            return _node('Statement', decl.matched_string, [decl])

        # Label  identifier :
        if tok.type == TT.IDENT and self._peek(1).type == TT.COLON:
            name = self._consume().value
            self._consume(TT.COLON)
            return _node('Statement', name + ':', [_node('Label', name)])

        # Standard assignment  identifier =
        if tok.type == TT.IDENT and self._peek(1).type == TT.ASSIGN:
            inner = self._parse_standard_assignment()
            self._consume(TT.SEMICOLON)
            assign = _node('Assignment', inner.matched_string, [inner])
            return _node('Statement', assign.matched_string, [assign])

        # Array assignment  identifier [ ... ] =
        if tok.type == TT.IDENT and self._peek(1).type == TT.LBRACKET:
            if self._is_array_assignment():
                inner = self._parse_array_assignment()
                self._consume(TT.SEMICOLON)
                assign = _node('Assignment', inner.matched_string, [inner])
                return _node('Statement', assign.matched_string, [assign])

        # Function-call statement  identifier (
        if tok.type == TT.IDENT and self._peek(1).type == TT.LPAREN:
            fc = self._parse_function_call()
            self._consume(TT.SEMICOLON)
            return _node('Statement', fc.matched_string, [fc])

        # Expression statement (covers standalone expressions)
        expr = self._parse_expression()
        self._consume(TT.SEMICOLON)
        return _node('Statement', expr.matched_string, [expr])

    def _is_array_assignment(self):
        """Peek forward past the matching ] and check whether = follows."""
        depth = 0
        i = self._pos
        lim = len(self._t)
        while i < lim:
            tt = self._t[i].type
            if tt == TT.LBRACKET:
                depth += 1
            elif tt == TT.RBRACKET:
                depth -= 1
                if depth == 0:
                    return (i + 1 < lim and
                            self._t[i + 1].type == TT.ASSIGN)
            elif tt in (TT.SEMICOLON, TT.EOF):
                return False
            i += 1
        return False

    # ── Declaration ───────────────────────────────────────────────

    def _parse_declaration(self):
        type_tok = self._consume()           # type keyword
        name_tok = self._consume(TT.IDENT)  # variable name
        type_node = _node('Type', type_tok.value)
        name_node = _node('Identifier', name_tok.value)

        if self._peek().type == TT.ASSIGN:
            self._consume(TT.ASSIGN)
            expr = self._parse_expression()
            matched = f'{type_tok.value} {name_tok.value} = {expr.matched_string}'
            return _node('Declaration', matched, [type_node, name_node, expr])

        matched = f'{type_tok.value} {name_tok.value}'
        return _node('Declaration', matched, [type_node, name_node])

    # ── Assignment ────────────────────────────────────────────────

    def _parse_standard_assignment(self):
        name_tok = self._consume(TT.IDENT)
        self._consume(TT.ASSIGN)
        expr = self._parse_expression()
        matched = f'{name_tok.value} = {expr.matched_string}'
        return _node('StandardAssignment', matched,
                     [_node('Identifier', name_tok.value), expr])

    def _parse_array_assignment(self):
        acc = self._parse_array_access()
        self._consume(TT.ASSIGN)
        expr = self._parse_expression()
        matched = f'{acc.matched_string} = {expr.matched_string}'
        return _node('ArrayAssignment', matched, [acc, expr])

    # ── Expression ────────────────────────────────────────────────

    def _parse_expression(self):
        left = self._parse_simple_expression()

        if self._peek().type in _REL_OPS:
            op_tok = self._consume()
            right = self._parse_simple_expression()
            op_node = _node('RelationalOperator', op_tok.value)
            matched = f'{left.matched_string} {op_tok.value} {right.matched_string}'
            rel = _node('RelationalExpression', matched, [left, op_node, right])
            return _node('Expression', matched, [rel])

        return _node('Expression', left.matched_string, [left])

    def _parse_simple_expression(self):
        term = self._parse_term()

        if self._peek().type in (TT.PLUS, TT.MINUS):
            op_tok = self._consume()
            right = self._parse_simple_expression()
            op_node = _node('AddOperator', op_tok.value)
            matched = f'{term.matched_string} {op_tok.value} {right.matched_string}'
            return _node('SimpleExpression', matched, [term, op_node, right])

        return _node('SimpleExpression', term.matched_string, [term])

    def _parse_term(self):
        factor = self._parse_factor()

        if self._peek().type in (TT.STAR, TT.SLASH):
            op_tok = self._consume()
            right = self._parse_term()
            op_node = _node('MultiplyOperator', op_tok.value)
            matched = f'{factor.matched_string} {op_tok.value} {right.matched_string}'
            return _node('Term', matched, [factor, op_node, right])

        return _node('Term', factor.matched_string, [factor])

    def _parse_factor(self):
        tok = self._peek()

        # Unary minus — applies to any factor (literal, identifier,
        # parenthesised expression, function call, array access).
        if tok.type == TT.MINUS:
            self._consume()
            inner = self._parse_factor()
            return _node('Factor', f'-{inner.matched_string}',
                         [_terminal('-'), inner])

        # Parenthesised expression  ( expr )
        if tok.type == TT.LPAREN:
            self._consume()
            expr = self._parse_expression()
            self._consume(TT.RPAREN)
            return _node('Factor', f'({expr.matched_string})',
                         [_terminal('('), expr, _terminal(')')])

        # Literal
        if tok.type in (TT.INT_LIT, TT.FLOAT_LIT, TT.STRING_LIT,
                        TT.CHAR_LIT, TT.TRUE, TT.FALSE):
            lit = self._parse_literal()
            return _node('Factor', lit.matched_string, [lit])

        # Identifier-based: function call, array access, plain identifier
        if tok.type == TT.IDENT:
            if self._peek(1).type == TT.LPAREN:
                fc = self._parse_function_call()
                return _node('Factor', fc.matched_string, [fc])
            if self._peek(1).type == TT.LBRACKET:
                acc = self._parse_array_access()
                return _node('Factor', acc.matched_string, [acc])
            name = self._consume().value
            return _node('Factor', name, [_node('Identifier', name)])

        raise SyntaxError(f"Unexpected token in expression: {tok!r}")

    # ── Literals ──────────────────────────────────────────────────

    def _parse_literal(self):
        tok = self._peek()
        if tok.type == TT.FLOAT_LIT:
            child = self._float_literal()
        elif tok.type == TT.INT_LIT:
            child = self._int_literal()
        elif tok.type == TT.STRING_LIT:
            self._consume()
            child = _node('StringLiteral', tok.value)
        elif tok.type == TT.CHAR_LIT:
            self._consume()
            child = _node('CharacterLiteral', tok.value)
        elif tok.type in (TT.TRUE, TT.FALSE):
            self._consume()
            child = _node('BooleanLiteral', tok.value)
        else:
            raise SyntaxError(f"Expected literal, got {tok!r}")
        # Literal node's matched_string is the raw text (used by evaluators)
        return _node('Literal', child.matched_string, [child])

    def _int_literal(self):
        tok = self._consume(TT.INT_LIT)
        return _node('IntegerLiteral', tok.value)

    def _float_literal(self):
        tok = self._consume(TT.FLOAT_LIT)
        return _node('FloatLiteral', tok.value)

    # ── Function call ─────────────────────────────────────────────

    def _parse_function_call(self):
        name_tok = self._consume(TT.IDENT)
        self._consume(TT.LPAREN)
        args = self._parse_argument_list()
        self._consume(TT.RPAREN)

        matched = f'{name_tok.value}({args.matched_string})'
        return _node('FunctionCall', matched,
                     [_node('Identifier', name_tok.value),
                      _terminal('('),
                      args,
                      _terminal(')')])

    def _parse_argument_list(self):
        # Empty argument list
        if self._peek().type == TT.RPAREN:
            return _node('ArgumentList', '')

        expr = self._parse_expression()

        if self._peek().type == TT.COMMA:
            self._consume()
            rest = self._parse_argument_list()
            matched = f'{expr.matched_string}, {rest.matched_string}'
            return _node('ArgumentList', matched,
                         [expr, _terminal(','), rest])

        return _node('ArgumentList', expr.matched_string, [expr])

    # ── Array access ──────────────────────────────────────────────

    def _parse_array_access(self):
        name_tok = self._consume(TT.IDENT)
        self._consume(TT.LBRACKET)
        idx = self._parse_expression()
        self._consume(TT.RBRACKET)
        matched = f'{name_tok.value}[{idx.matched_string}]'
        return _node('ArrayAccess', matched,
                     [_node('Identifier', name_tok.value),
                      _terminal('['),
                      idx,
                      _terminal(']')])


# ─── Public API ───────────────────────────────────────────────────────────────

def parseLine(line: str) -> SyntaxTreeNode:
    """
    Parse one preprocessed Orion source line.

    Returns a SyntaxTreeNode (Statement root) on success,
    or raises SyntaxError on failure.
    """
    tokens = tokenize(line)
    parser = _Parser(tokens)
    tree = parser.parse_statement()
    if parser._peek().type != TT.EOF:
        raise SyntaxError(
            f"Unexpected trailing tokens after statement: {parser._peek()!r}")
    return tree
