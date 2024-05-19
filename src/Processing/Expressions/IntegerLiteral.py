def evaluate(ctx, IntegerLiteralNode):
    return int(IntegerLiteralNode.matched_string)