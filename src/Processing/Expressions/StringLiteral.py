def evaluate(ctx, StringLiteralNode):
    return StringLiteralNode.matched_string[1:-1]