from ..Expression import evaluateExpression
from ...LangData.oDataTypes import oFloat, oString
from ...LangData.exceptions import ArgumentError

def execute(ctx, args):
    if len(args) != 1:
        raise ArgumentError("StringToFloat expected 1 argument, got",len(args))
    
    value = evaluateExpression(ctx, args[0])

    if not isinstance(value, oString):
        raise ValueError("StringToFloat requires input of type String")
    
    if value.getValue() is None:
        raise ValueError("null provided")
    
    try:
        float(value.getValue())
    except ValueError:
        raise ValueError(f"Attempted to convert {value.getValue()} to float")
    
    return oFloat(float(value.getValue()))
        
    
