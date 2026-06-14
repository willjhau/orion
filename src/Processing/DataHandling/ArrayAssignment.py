from ...LangData.oDataStructures import oArray
from .. import Expression

def handleArrayAssignment(ctx, arrayAssignmentNode):
    """
    Execute an array element assignment.

    Tree structure (produced by the parser):
        ArrayAssignment
            ArrayAccess      children[0]
                Identifier   — array variable name
                '['
                Expression   — index expression
                ']'
            Expression       children[1]  — value to assign
    """
    acc_node  = arrayAssignmentNode.children[0]   # ArrayAccess
    val_node  = arrayAssignmentNode.children[1]   # Expression

    name  = acc_node.children[0].matched_string
    array = ctx.getDataMap().getData(name)

    if not isinstance(array, oArray):
        raise TypeError(f"Variable '{name}' is not an array")

    index_val = Expression.evaluateExpression(ctx, acc_node.children[2])
    index = index_val.getValue()

    if not isinstance(index, int):
        raise TypeError(f"Array index must be an integer, got {type(index)}")

    value = Expression.evaluateExpression(ctx, val_node)
    array.setElement(index, value)
