from ...LangData.oDataTypes import oBool

def evaluate(ctx, BooleanLiteralNode):
    if BooleanLiteralNode.matched_string == 'true':
        return oBool(True)
    else:
        return oBool(False)