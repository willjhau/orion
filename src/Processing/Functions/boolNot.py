from ...LangData.exceptions import ArgumentError
from ...Processing.Expression import evaluateExpression
from ...LangData.oDataTypes import oBool

def execute(ctx, args):
    if len(args) != 1:
        raise ArgumentError("Expected 1 argument, got",len(args))
    
    value = evaluateExpression(ctx, args[0])

    if not isinstance(value, oBool):
        raise ValueError("not must be applied to a boolean type")
    
    return oBool(not value.getValue())