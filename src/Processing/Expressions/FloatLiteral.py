from ...LangData.oDataTypes import oFloat

def evaluate(ctx, FloatLiteralNode):
    return oFloat(float(FloatLiteralNode.matched_string))