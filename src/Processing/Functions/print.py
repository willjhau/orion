from ..Expression import evaluateExpression
from ...LangData.oDataTypes import oBool
def execute(ctx, args):
    if len(args) == 0:
        print()
        return
    
    message = ""
    for arg in args:
        add = evaluateExpression(ctx, arg).getValue()
        if isinstance(add, oBool):
            if add is True:
                message += 'true '
            elif add is False:
                message += 'false '
            else:
                message += ''
        else:
            message += str(add) + " "

    print(message[:-1])
    return 