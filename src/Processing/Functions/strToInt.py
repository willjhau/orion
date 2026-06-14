from ..Expression import evaluateExpression
from ...LangData.oDataTypes import oInt, oString
from ...LangData.exceptions import ArgumentError

def execute(ctx, args):
    if len(args) != 1:
        raise ArgumentError("StringToInt expected 1 argument, got",len(args))
    
    value = evaluateExpression(ctx, args[0])

    if not isinstance(value, oString):
        raise ValueError("StringToInt requires input of type String")
    
    if value.getValue() is None:
        raise ValueError("null provided")
    
    try:
        parsed = int(value.getValue())
    except ValueError:
        raise ValueError(f"Cannot convert {value.getValue()!r} to int")

    return oInt(parsed)
        
    
