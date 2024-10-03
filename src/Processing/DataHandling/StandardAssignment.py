from ...Processing import Expression

def handleStandardAssignment(ctx, StandardAssignmentNode):
    name = StandardAssignmentNode.children[0].matched_string
    value = Expression.evaluateExpression(ctx, StandardAssignmentNode.children[1])
    
    if not ctx.getDataMap().checkIfDataExists(name):
        raise Exception("Variable not declared: " + name)
    
    if not ctx.getDataMap().getData(name).isValid(value):
        raise Exception("Invalid value for variable " + name + ": " + str(value))
    
    ctx.getDataMap().setData(name, value)
    return