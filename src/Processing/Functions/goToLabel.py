from ...Processing.Expression import evaluateExpression
from ...LangData.oDataTypes import oDataType
from ...LangData.exceptions import ArgumentError

def execute(ctx, args):
    if len(args) == 1:
        label = None
        try:
            label = args[0].matched_string
        except IndexError:
            raise IndexError("No label provided")
        if label is None:
            raise ValueError("No label provided")
        try:
            address = ctx.getLabelMap().getAddressFromLabel(label)
        except:
            raise NameError("Label not found")
        # Exception is raised during ctx.getLabelMap, we don't need to consider it here

        ctx.getInstructionMemory().jumpTo(address)
        return
    else:
        raise ArgumentError("goToLabel() expects exactly 1 argument")
