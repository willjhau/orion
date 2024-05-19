def evaluate(ctx, BooleanLiteralNode):
    return BooleanLiteralNode.matched_string == 'true'