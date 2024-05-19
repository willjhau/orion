from .Functions import print
from .Functions import takeInput
from .Functions import goToLabel
from .Functions import strToInt
from .Functions import intToStr
from .Functions import strToFloat
from .Functions import floatToStr
from .Functions import boolToStr
from .Functions import charToInt
from .Functions import intToChar
from .Functions import jumpIf
from .Functions import boolNot
from .Functions import boolAnd
from .Functions import boolOr
from .Functions import boolXor

def argTreeToArgList(functionCallNode):
    print(functionCallNode.children)
    if len(functionCallNode.children) == 0:
        return []
    if len(functionCallNode.children) == 1:
        return [functionCallNode.children[0]]
    return [functionCallNode.children[0]] + argTreeToArgList(functionCallNode.children[1])

def executeFunction(ctx, functionCallNode):
    if functionCallNode.children[0].symbol.name == "print":
        return print.execute(ctx, argTreeToArgList(functionCallNode.children[2]))

    if functionCallNode.children[0].symbol.name == "takeInput":
        return takeInput.execute(ctx, argTreeToArgList(functionCallNode.children[2]))
    
    if functionCallNode.children[0].symbol.name == "goToLabel":
        return goToLabel.execute(ctx, argTreeToArgList(functionCallNode.children[2]))