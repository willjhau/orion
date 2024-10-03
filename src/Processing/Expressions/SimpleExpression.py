from . import Term
from ...LangData.oDataTypes import *

def evaluateSimpleExpression(ctx, expression):
    if len(expression.children) == 1:
        return Term.evaluateTerm(ctx, expression.children[0])
    
    elif len(expression.children) == 3:

        arg1 = Term.evaluateTerm(ctx, expression.children[0])
        arg2 = evaluateSimpleExpression(ctx, expression.children[2])
        
        if expression.children[1].matched_string == "+":
            if type(arg1) == oString and type(arg2) == oString:
                return oString(str(arg1.getValue()) + str(arg2.getValue()))
            
            elif type(arg1) == oInt and type(arg2) == oInt:
                return oInt(arg1.getValue() + arg2.getValue())
            
            elif type(arg1) == oFloat and type(arg2) == oFloat:
                return oFloat(arg1.getValue() + arg2.getValue())
            
            elif type(arg1) == oInt and type(arg2) == oFloat:
                return oFloat(arg1.getValue() + arg2.getValue())
            
            elif type(arg1) == oFloat and type(arg2) == oInt:
                return oFloat(arg1.getValue() + arg2.getValue())
            
            elif type(arg1) == oString and type(arg2) == oChar:
                return oString(str(arg1.getValue()) + str(arg2.getValue()))
            
            elif type(arg1) == oChar and type(arg2) == oString:
                return oString(str(arg1.getValue()) + str(arg2.getValue()))
            
            elif type(arg1) == oChar and type(arg2) == oChar:
                return oString(str(arg1.getValue()) + str(arg2.getValue()))
            
            else:
                raise Exception("Type mismatch in addition")
            
        if expression.children[1].matched_string == "-":
            if type(arg1) == oInt and type(arg2) == oInt:
                return oInt(arg1.getValue() - arg2.getValue())
            
            elif type(arg1) == oFloat and type(arg2) == oFloat:
                return oFloat(arg1.getValue() - arg2.getValue())
            
            elif type(arg1) == oInt and type(arg2) == oFloat:
                return oFloat(arg1.getValue() - arg2.getValue())
            
            elif type(arg1) == oFloat and type(arg2) == oInt:
                return oFloat(arg1.getValue() - arg2.getValue())
            
            else:
                raise Exception("Type mismatch in subtraction")