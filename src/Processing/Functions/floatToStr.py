from ..Expression import evaluateExpression
from ...LangData.oDataTypes import oFloat, oString
from ...LangData.exceptions import ArgumentError

def execute(ctx, args):
    if len(args) != 1:
        raise ArgumentError("floatToString expected 1 argument, got",len(args))
    
    value = evaluateExpression(ctx, args[0])

    if not isinstance(value, oFloat):
        raise ValueError("floatToString requires input of type float")
    
    if value.getValue() is None:
        raise ValueError("null provided")
    
    return oString(str(value.getValue()))
    
