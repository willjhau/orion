from ...Processing.Expression import evaluateExpression
from ...LangData.oDataTypes import oString
from ...LangData.exceptions import ArgumentError

def execute(ctx, args):
    if len(args) == 1:
        try:
            label = evaluateExpression(ctx, args[0])
        except IndexError:
            raise IndexError("No label provided")
        if not isinstance(label, oString):
            raise NameError("Invalid label name")
        
        address = ctx.getLabelMap().getAddressFromLabel(label.getValue())
        # Exception is raised during ctx.getLabelMap, we don't need to consider it here

        ctx.getInstructionMemory().jumpTo(address)
        return
    else:
        raise ArgumentError("goToLabel() expects exactly 1 argument")
