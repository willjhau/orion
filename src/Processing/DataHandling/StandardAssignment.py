from ...Processing import Expression
def handleStandardAssignment(ctx, StandardAssignmentNode):
    name = StandardAssignmentNode.children[0].matched_string
    value = Expression.evaluateExpression(ctx, StandardAssignmentNode.children[1])
    
    if name not in ctx.getDataMap():
        raise Exception("Variable not declared: " + name)
    
    if not ctx.getDataMap()[name].isValid(value):
        raise Exception("Invalid value for variable " + name + ": " + str(value))
    
    ctx.getDataMap()[name].setValue(value)
    return