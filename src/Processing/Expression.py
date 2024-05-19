from .Expressions import SimpleExpression
from .Expressions import RelationalExpression

def evaluateExpression(ctx, expression):
    if expression.children[0].symbol.name == "SimpleExpression":
        return SimpleExpression.evaluateSimpleExpression(ctx, expression.children[0])
    elif expression.children[0].symbol.name == "RelationalExpression":
        return RelationalExpression.evaluateRelationalExpression(ctx, expression.children[0])