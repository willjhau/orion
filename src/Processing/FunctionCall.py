from .Functions import Print
from .Functions import TakeInput
from .Functions import GoToLabel
from .Functions import StrToInt
from .Functions import IntToStr
from .Functions import StrToFloat
from .Functions import FloatToStr
from .Functions import BoolToStr
from .Functions import CharToInt
from .Functions import IntToChar
from .Functions import JumpIf
from .Functions import BoolNot
from .Functions import BoolAnd
from .Functions import BoolOr
from .Functions import BoolXor

def argTreeToArgList(functionCallNode):
    # Check if the function call has any arguments
    if len(functionCallNode.children) == 0:
        return []
    
    # If the function call has only one argument
    if len(functionCallNode.children) == 1:
        return [functionCallNode.children[0]]
    
    # If the function call has more than one argument
    return [functionCallNode.children[0]] + argTreeToArgList(functionCallNode.children[2])


def executeFunction(ctx, functionCallNode):
    if functionCallNode.children[0].matched_string == "print":
        return Print.execute(ctx, argTreeToArgList(functionCallNode.children[2]))

    elif functionCallNode.children[0].matched_string == "takeInput":
        return TakeInput.execute(ctx, argTreeToArgList(functionCallNode.children[2]))
    
    elif functionCallNode.children[0].matched_string == "goToLabel":
        return GoToLabel.execute(ctx, argTreeToArgList(functionCallNode.children[2]))
    
    elif functionCallNode.children[0].matched_string == "and":
        return BoolAnd.execute(ctx, argTreeToArgList(functionCallNode.children[2]))
    
    elif functionCallNode.children[0].matched_string == "not":
        return BoolNot.execute(ctx, argTreeToArgList(functionCallNode.children[2]))
    
    elif functionCallNode.children[0].matched_string == "or":
        return BoolOr.execute(ctx, argTreeToArgList(functionCallNode.children[2]))
    
    elif functionCallNode.children[0].matched_string == "boolToString":
        return BoolToStr.execute(ctx, argTreeToArgList(functionCallNode.children[2]))
    
    elif functionCallNode.children[0].matched_string == "xor":
        return BoolXor.execute(ctx, argTreeToArgList(functionCallNode.children[2]))
    
    # elif functionCallNode.children[0].matched_string == "not":
    #     return BoolNot.execute(ctx, argTreeToArgList(functionCallNode.children[2]))
    
    else:
        raise NameError(f"Unknown function name: {functionCallNode.children[0].matched_string}")