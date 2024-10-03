from ..Expression import evaluateExpression
from ...LangData.oDataTypes import oBool, oString
from ...LangData.exceptions import ArgumentError

def execute(ctx, args):
    if len(args) != 1:
        raise ArgumentError("boolToString expected 1 argument, got",len(args))
    
    value = evaluateExpression(ctx, args[0])

    if not isinstance(value, oBool):
        raise ValueError("boolToString requires input of type boolean")
    
    if value.getValue() is True:
        return oString('true')
    elif value.getValue() is False:
        return oString('false')
    else:
        raise ValueError("null provided")
    
