from ..Expression import evaluateExpression
def execute(ctx, *args):
    if len(args) == 0:
        print()
        return
    
    message = ""

    for arg in args:
        message += str(evaluateExpression(ctx, arg)) + " "

    print(message[:-1])
    return 