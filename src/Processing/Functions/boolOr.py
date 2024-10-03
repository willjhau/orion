from ..Expression import evaluateExpression
from ...LangData.exceptions import ArgumentError
from ...LangData.oDataTypes import oBool

def execute(ctx, args):
    if len(args) == 0:
        raise ArgumentError("Expected at least one argument, got 0")
    
    processedArgs = [evaluateExpression(ctx, arg).getValue() for arg in args]
    if not all([isinstance(arg, oBool) for arg in processedArgs]):
        raise ValueError("or must take boolean values as inputs")
    
    truth = [arg is True for arg in processedArgs]
    if any(truth):
        return oBool(True)
    
    return oBool(False)

