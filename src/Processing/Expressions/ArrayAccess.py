from .. import Expression
from ...LangData.oDataStructures import oArray

def handleArrayAccess(ctx, arrayAccessNode):
    array = ctx.getDataMap()(arrayAccessNode.children[0].matched_string)
    if not array.isinstance(oArray):
        raise Exception("Variable is not an array: " + arrayAccessNode.children[0].matched_string)
    
    index = Expression.evaluateExpression(ctx, arrayAccessNode.children[2])
    if not isinstance(index, int):
        raise Exception("Array index must be an integer")
    
    if index >= array.getSize():
        raise Exception("Array index out of bounds")
    
    return array[index]