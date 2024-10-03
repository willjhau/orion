from ...LangData.oDataTypes import oChar

def evaluate(ctx, CharacterLiteralNode):
    return oChar(CharacterLiteralNode.matched_string[1:-1])