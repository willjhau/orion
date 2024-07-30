def evaluate(ctx, CharacterLiteralNode):
    return CharacterLiteralNode.matched_string[1:-1]