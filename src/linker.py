from src.labelMap import LabelMap
from src.programCounter import ProgramCounter
from src.instructionMemory import InstructionMemory
from src.exceptions import AddressError
from src.Grammar.SyntaxTree import SyntaxTreeNode

class Linker:
    def __init__(self, codeTrees: list):
        self.__labelMap = LabelMap()
        self.__instructionMemory = InstructionMemory()
        self.__codeTrees = codeTrees
        self.fillMemory()

    def fillMemory(self):
        i = 0
        while i < len(self.__codeTrees):
            tree:SyntaxTreeNode = self.__codeTrees[i]
            if tree.children[0].symbol == "Label":
                self.__labelMap.addLabel(tree.children[0].matched_string, i)
            else:
                self.__instructionMemory.addInstruction(tree)
                i += 1
    
    def getInstructionMemory(self):
        return self.__instructionMemory
    
    def getLabelMap(self):
        return self.__labelMap