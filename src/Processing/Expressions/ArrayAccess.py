from .. import Expression
from ...LangData.oDataStructures import oArray

def evaluate(ctx, arrayAccessNode):
    """
    Evaluate an ArrayAccess node.

    Tree structure (produced by the parser):
        ArrayAccess
            Identifier   children[0]  — array variable name
            '['          children[1]
            Expression   children[2]  — index expression
            ']'          children[3]
    """
    name  = arrayAccessNode.children[0].matched_string
    array = ctx.getDataMap().getData(name)

    if not isinstance(array, oArray):
        raise TypeError(f"Variable '{name}' is not an array")

    index_val = Expression.evaluateExpression(ctx, arrayAccessNode.children[2])
    index = index_val.getValue()

    if not isinstance(index, int):
        raise TypeError(f"Array index must be an integer, got {type(index)}")

    return array.getElement(index)
