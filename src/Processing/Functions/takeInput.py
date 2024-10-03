from ...LangData.exceptions import ArgumentError
from ...LangData.oDataTypes import oString
from ...Processing.Expression import evaluateExpression

def execute(ctx, args):
    if len(args) == 0:
        inputValue = input()
    elif len(args) == 1:
        try:
            value = str(evaluateExpression(ctx, args[0]).getValue())
            inputValue = input(value)
        except IndexError:
            inputValue = input()
    else:
        raise ArgumentError("takeInput() requires at most 1 argument")
    return oString(inputValue)
