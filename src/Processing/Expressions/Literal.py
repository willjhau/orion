from . import StringLiteral
from . import CharacterLiteral
from . import IntegerLiteral
from . import FloatLiteral
from . import BooleanLiteral

def evaluateLiteral(ctx, literalNode):
    if literalNode.children[0].symbol.name == "StringLiteral":
        return StringLiteral.evaluate(ctx, literalNode)
    
    if literalNode.children[0].symbol.name == "CharacterLiteral":
        return CharacterLiteral.evaluate(ctx, literalNode)
    
    if literalNode.children[0].symbol.name == "IntegerLiteral":
        return IntegerLiteral.evaluate(ctx, literalNode)
    
    if literalNode.children[0].symbol.name == "FloatLiteral":
        return FloatLiteral.evaluate(ctx, literalNode)
    
    if literalNode.children[0].symbol.name == "BooleanLiteral":
        return BooleanLiteral.evaluate(ctx, literalNode)
    