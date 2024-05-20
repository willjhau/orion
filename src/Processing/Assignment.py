from .DataHandling import ArrayAssignment
from .DataHandling import StandardAssignment
def executeAssignment(ctx, AssignmentNode):
    if AssignmentNode.children[0].symbol.name == "StandardAssignment":
        return StandardAssignment.handleStandardAssignment(ctx, AssignmentNode.children[0])
    
    elif AssignmentNode.children[0].symbol.name == "ArrayAssignment":
        return ArrayAssignment.handleArrayAssignment(ctx, AssignmentNode.children[0])
    
