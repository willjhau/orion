from . import Term

def evaluateSimpleExpression(ctx, expression):
    if len(expression.children) == 1:
        return Term.evaluateTerm(ctx, expression.children[0])
    elif len(expression.children) == 3:
        arg1 = Term.evaluateTerm(ctx, expression.children[0])
        arg2 = evaluateSimpleExpression(ctx, expression.children[2])
        if expression.children[1].matched_string == "+":
            return arg1 + arg2
        if expression.children[1].matched_string == "-":
            return arg1 - arg2