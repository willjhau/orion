from ..Expression import evaluateExpression
from ...LangData.oDataTypes import oInt, oString
from ...LangData.exceptions import ArgumentError

def execute(ctx, args):
    if len(args) != 1:
        raise ArgumentError("intToString expected 1 argument, got",len(args))
    
    value = evaluateExpression(ctx, args[0])

    if not isinstance(value, oInt):
        raise ValueError("intToString requires input of type int")
    
    if value.getValue() is None:
        raise ValueError("null provided")
    
    return oString(str(value.getValue()))
    
