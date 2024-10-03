from ...LangData.oDataTypes import oInt

def evaluate(ctx, IntegerLiteralNode):
    return oInt(int(IntegerLiteralNode.matched_string))