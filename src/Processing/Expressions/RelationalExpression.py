from . import SimpleExpression

def evaluateRelationalExpression(ctx, expression):
    arg1 = SimpleExpression.evaluateSimpleExpression(ctx, expression.children[0])
    arg2 = SimpleExpression.evaluateSimpleExpression(ctx, expression.children[2])

    if expression.children[1].matched_string == "<":
        return arg1 < arg2
    
    if expression.children[1].matched_string == ">":
        return arg1 > arg2
    
    if expression.children[1].matched_string == "<=":
        return arg1 <= arg2
    
    if expression.children[1].matched_string == ">=":
        return arg1 >= arg2
    
    if expression.children[1].matched_string == "==":
        return arg1 == arg2
    
    if expression.children[1].matched_string == "!=":
        return arg1 != arg2
    
    raise Exception("Unknown relational operator: " + expression.children[1].matched_string)
