import sys
from ..Structures.syntaxTree import SyntaxTreeNode
# sys.stdout = open('output.txt', 'w')

def generateIdentifiers(string):
    identifiers = []
    current = ''
    for char in string:
        if char.isalnum():
            current += char
        else:
            if current:
                identifiers.append(current)
            current = ''
    if current:
        identifiers.append(current)
    
    # convert each element to a set to remove duplicates and then back to a list
    identifiers = list(set(identifiers))

    # convert each element into the form &e1 &e2 &e3 ... for each character in the identifier
    for i in range(len(identifiers)):
        identifiers[i] = (''.join([f'&{char} ' for char in identifiers[i]]))[:-1]
    
    # return the list ordered from the longest identifier to the shortest
    return sorted(identifiers, key=lambda x: len(x), reverse=True)


def maxArrayDepth(string):
    maxDepth = 0
    currentDepth = 0
    for char in string:
        if char == '[':
            currentDepth += 1
            if currentDepth > maxDepth:
                maxDepth = currentDepth
        elif char == ']':
            currentDepth -= 1
    return maxDepth

def generateIntegerLiterals(string):
    literals = []
    current = ''
    for char in string:
        if char.isdigit():
            current += char
        else:
            if current:
                literals.append(current)
            current = ''
    if current:
        literals.append(current)
    
    literals = list(set(literals))
    for i in range(len(literals)):
        literals[i] = (''.join([f'&{char} ' for char in literals[i]]))[:-1]

    # return the list ordered from the longest integer to the shortest
    return sorted(literals, key=lambda x: len(x), reverse=True)

def generateStringLiterals(string):
    if '"' not in string:
        return []
    
    if string.count('"') % 2 != 0:
        return []

    literals = []
    current = ''
    inString = False
    for char in string:
        if char == '"':
            if inString:
                literals.append(current)
                current = ''
            inString = not inString
        elif inString:
            current += char
    if current:
        literals.append(current)

    literals = list(set(literals))
    for i in range(len(literals)):
        current = ''
        for char in literals[i]:
            if char == ' ':
                current += '$ '
            else:
                current += f'&{char} '
        literals[i] = current[:-1]
    # return the list ordered from the longest string to the shortest
    return sorted(literals, key=lambda x: len(x), reverse=True)
    


def generateCharacterLiterals(string):
    noDuplicates = list(set(string.split("'")))
    filtered = []
    for i, s in enumerate(noDuplicates):
        if s == '':
            noDuplicates[i] = '~NULLSYMBOL~'
        elif len(s) == 1:
            filtered.append(f'&{s}')
    return filtered

def generate_combinations(arrays):
    def generate_recursive(current, depth):
        if depth == len(arrays):
            yield current
            return
        for value in arrays[depth]:
            yield from generate_recursive(current + [value], depth + 1)
    
    yield from generate_recursive([], 0)


def readGrammar(filename, inputString):
    symbols = {}
    rules = []

    def get_symbol(name, terminal=False):
        if name not in symbols:
            symbols[name] = Symbol(name, terminal)
        return symbols[name]

    with open(filename, 'r') as file:
        lines = file.readlines()

        identifiers = [f'Identifier -> {id}' for id in generateIdentifiers(inputString)]
        lines.extend(identifiers)
        string_literals = [f'String -> {lit}' for lit in generateStringLiterals(inputString)]
        lines.extend(string_literals)
        integer_literals = [f'IntegerLiteral -> {lit}' for lit in generateIntegerLiterals(inputString)]
        lines.extend(integer_literals)
        character_literals = [f'Character -> {lit}' for lit in generateCharacterLiterals(inputString)]
        lines.extend(character_literals)


        for line in lines:
            line = line.strip()
            if not line:
                continue

            left_part, right_part = line.split('->')
            left_symbol = get_symbol(left_part.strip())

            right_symbols = []

            for part in right_part.strip().split():
                if part == "$":
                    right_symbols.append([get_symbol(' ', terminal=True)])
                elif part == '~':
                    right_symbols.append([get_symbol('~NULLSYMBOL~', terminal=True)])
                elif part.startswith('`') and part.endswith('`'):
                    right_symbols.append([])
                    for symbol in part[1:-1]:
                        right_symbols[-1].append(get_symbol(symbol, terminal=True))
                elif part.startswith('&'):
                    # if len(part) == 1:
                    #     right_symbols.append([get_symbol(' ', terminal=True)])
                    right_symbols.append([get_symbol(part[1:], terminal=True)])
                else:
                    right_symbols.append([get_symbol(part)])
            for configuration in generate_combinations(right_symbols):
                rules.append(Rule(left_symbol, configuration))
        
    return rules

class Symbol:
    def __init__(self, name, terminal = False):
        self.name = name
        self.terminal: bool = terminal

    def getRules(self, rules):
        return [rule for rule in rules if rule.left == self]

    def isTerminal(self):
        return self.terminal

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'

class Rule:
    def __init__(self, left, right):
        if not isinstance(left, Symbol):
            raise ValueError('Left side of a rule must be a Symbol')
        # Left must be a non-terminal Symbol
        if left.isTerminal():
            raise ValueError('Left side of a rule must be a non-terminal Symbol')
        # Right must be a list of Symbols
        if not all([isinstance(symbol, Symbol) for symbol in right]):
            raise ValueError('Right side of a rule must be a list of Symbols')
        self.left = left
        self.right = right
    


def parse(input_string, start_symbol, RULES, verbose, MAX_DEPTH = 100):
    def dfs(symbol, input_string, pos, verbose, depth=0):
        if depth > MAX_DEPTH:
            return -1, None
        if verbose:
            print(f'Current symbol: {symbol.name}, input string: {input_string[pos:]}')

        # If the current symbol is a terminal, match it with the input
        if symbol.terminal:
            if verbose:
                if pos >= len(input_string):
                    print(f'End of input string reached. No match found for terminal symbol {symbol.name}')
            if symbol.name == '~NULLSYMBOL~':
                return pos, SyntaxTreeNode(symbol, '')
            
            elif pos < len(input_string) and input_string[pos] == symbol.name:
                if verbose:
                    print(f'Match found for terminal symbol {symbol.name}')
                    print(f'Returning position {pos + 1}')
                node = SyntaxTreeNode(symbol, input_string[pos:pos+1])
                return pos + 1, node  # Move to the next character in the input string
            else:
                return -1, None # No match found

        if verbose:
            print(f'Current symbol {symbol.name} is a non-terminal')
        # If the current symbol is a non-terminal, try all its production rules
        rules = symbol.getRules(RULES)
        if verbose: 
            for rule in rules:
                print(f'Rule {rule.left.name} -> {" ".join([str(symbol) for symbol in rule.right])}')
        for rule in rules:
            if verbose:
                print(f'Trying rule {rule.left.name} -> {" ".join([str(symbol) for symbol in rule.right])}')
            current_pos = pos
            match = True
            currentNode = SyntaxTreeNode(symbol, '')
            for sub_symbol in rule.right:
                if verbose:
                    print(f'Parsing symbol {sub_symbol.name} starting from position {current_pos}')
                    print(f'Executing DFS on symbol {sub_symbol.name} with input string {input_string[current_pos:]}')
                current_pos, childNode = dfs(sub_symbol, input_string, current_pos, verbose, depth + 1)
                if current_pos == -1:
                    if verbose:
                        print(f'No match found for symbol {sub_symbol.name}')

                    match = False
                    break
                else:
                    currentNode.add_child(childNode)
            if match:
                currentNode.matched_string = input_string[pos:current_pos]
                if verbose:
                    print(f'Match found for rule {rule.left.name} -> {" ".join([str(symbol) for symbol in rule.right])}')
                    print(f'Returning position {current_pos}')
                return current_pos, currentNode

        return -1, None  # No match found

    # Start the DFS from the start symbol and the beginning of the input string
    final_pos, syntaxTree = dfs(start_symbol, input_string, 0, verbose)

    if final_pos == len(input_string):
        return syntaxTree
    return {}

def convertLineToSyntaxTree(line):
    RULES = readGrammar('grammar.txt', line)
    startSymbol = RULES[0].left
    return parse(line, startSymbol, RULES, False)

if __name__ == '__main__':
    # inputString = 'q[0] = 1;'
    # RULES = readGrammar('grammar.txt', inputString)
    verbose = False
    # verbose = True

    with open('sampleCode.orion', 'r') as f:
        for line in f:
            inputString = line.strip()
            RULES = readGrammar('grammar.txt', inputString)
            print(f'Parsing input string: {inputString}')
            result = parse(inputString, RULES[0].left, RULES, verbose)
            print(result)

    # if verbose:
    #     for rule in RULES:
    #         print(f'{rule.left.name} -> {" ".join([str(symbol) for symbol in rule.right])}')

    # startSymbol = RULES[0].left

    # result = parse(inputString, startSymbol, RULES, verbose)
    # print(result)