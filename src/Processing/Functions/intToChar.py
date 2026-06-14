from ..Expression import evaluateExpression
from ...LangData.oDataTypes import oChar, oInt
from ...LangData.exceptions import ArgumentError

def execute(ctx, args):
    if len(args) != 1:
        raise ArgumentError("inToChar expected 1 argument, got",len(args))
    
    value = evaluateExpression(ctx, args[0])

    if not isinstance(value, oInt):
        raise ValueError("intToChar requires input of type char")
    
    if value.getValue() is None:
        raise ValueError("null provided")
    
    return oChar(chr(value.getValue()))
    
