from .labelMap import LabelMap
from .programCounter import ProgramCounter
from .instructionMemory import InstructionMemory
from .exceptions import AddressError

class Linker:
    def __init__(self, codeTrees: list, path: str):
        self.__labelMap = LabelMap()
        self.__instructionMemory = InstructionMemory(path)
        self.__codeTrees = codeTrees
        self.fillMemory()

    def fillMemory(self):
        i = 0
        while i < len(self.__codeTrees):
            tree = self.__codeTrees[i]
            if tree.children[0].symbol == "Label":
                self.__labelMap.addLabel(tree.children[0].matched_string, i)
            else:
                self.__instructionMemory.addInstruction(tree)
                i += 1
    
    def getInstructionMemory(self):
        return self.__instructionMemory
    
    def getLabelMap(self):
        return self.__labelMap