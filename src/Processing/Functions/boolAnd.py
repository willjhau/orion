from ..Expression import evaluateExpression
def execute(ctx, *args):
    if len(args) != 2:
        raise Exception("Expected 2 arguments, got " + str(len(args)))

    arg1 = evaluateExpression(ctx, arg1)
    arg2 = evaluateExpression(ctx, arg2)

    if arg1 is True and arg2 is True:
        return True
    
    return False

