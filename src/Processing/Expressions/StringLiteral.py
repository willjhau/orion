from ...LangData.oDataTypes import oString

def evaluate(ctx, StringLiteralNode):
    return oString(StringLiteralNode.matched_string[1:-1])