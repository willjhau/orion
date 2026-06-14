from ...Processing.Expression import evaluateExpression

def execute(ctx, args):
    exp = evaluateExpression(ctx, args[0]).getValue()
    if exp is True:
        try:
            address = ctx.getLabelMap().getAddressFromLabel(args[1].matched_string)
        except:
            raise NameError(f"Address label {args[1].matched_string} not found")
        
        ctx.getInstructionMemory().jumpTo(address)