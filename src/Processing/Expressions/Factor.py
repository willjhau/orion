from . import Literal
from .. import FunctionCall
from . import ArrayAccess
from .. import Expression
from ...LangData.oDataTypes import oFloat, oInt

def evaluateFactor(ctx, factor):
    if len(factor.children) == 1:
        if factor.children[0].symbol.name == "Literal":
            return Literal.evaluateLiteral(ctx, factor.children[0])

        if factor.children[0].symbol.name == 'FunctionCall':
            return FunctionCall.executeFunction(ctx, factor.children[0])

        if factor.children[0].symbol.name == 'ArrayAccess':
            return ArrayAccess.evaluate(ctx, factor.children[0])

        if factor.children[0].symbol.name == 'Identifier':
            return ctx.getDataMap().getData(factor.children[0].matched_string)

    if len(factor.children) == 2:
        # Unary minus: '-' Factor
        inner = evaluateFactor(ctx, factor.children[1])
        v = inner.getValue()
        if isinstance(v, bool) or not isinstance(v, (int, float)):
            raise TypeError("Unary '-' requires a numeric operand")
        if isinstance(v, int):
            return oInt(-v)
        return oFloat(-v)

    if len(factor.children) == 3:
        # Parenthesised expression: '(' Expression ')'
        return Expression.evaluateExpression(ctx, factor.children[1])
