from . import SimpleExpression
from ...LangData.oDataTypes import *

def evaluateRelationalExpression(ctx, expression):
    arg1 = SimpleExpression.evaluateSimpleExpression(ctx, expression.children[0])
    arg2 = SimpleExpression.evaluateSimpleExpression(ctx, expression.children[2])

    if type(arg1) != type(arg2):
        raise Exception("Type mismatch in relational expression")
    

    if (type(arg1) == oInt or type(arg1) == oFloat):

        arg1 = arg1.getValue()
        arg2 = arg2.getValue()

        if expression.children[1].matched_string == "<":
            return oBool(arg1 < arg2)
        
        if expression.children[1].matched_string == ">":
            return oBool(arg1 > arg2)
        
        if expression.children[1].matched_string == "<=":
            return oBool(arg1 <= arg2)
        
        if expression.children[1].matched_string == ">=":
            return oBool(arg1 >= arg2)
    
    else:
        arg1 = arg1.getValue()
        arg2 = arg2.getValue()

    if expression.children[1].matched_string == "==":
        return oBool(arg1 == arg2)
    
    if expression.children[1].matched_string == "!=":
        return oBool(arg1 != arg2)
    
    raise Exception("Unknown relational operator: " + expression.children[1].matched_string)
