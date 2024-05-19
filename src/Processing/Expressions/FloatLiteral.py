def evaluate(ctx, FloatLiteralNode):
    return float(FloatLiteralNode.matched_string)