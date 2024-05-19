from ..Structures.labelMap import LabelMap
from ..Structures.programCounter import ProgramCounter
from ..Structures.instructionMemory import InstructionMemory
from ..LangData.exceptions import AddressError

class Linker:
    def __init__(self, codeTrees: list, path: str):
        self.__labelMap = LabelMap()
        self.__instructionMemory = InstructionMemory(path)
        self.__codeTrees = codeTrees
        self.fillMemory()

    def fillMemory(self):
        i = 0
        for tree in self.__codeTrees:
            if tree.children[0].symbol.name == "Label":
                self.__labelMap.addLabel(tree.children[0].matched_string, i)
            else:
                self.__instructionMemory.addInstruction(tree)
                i += 1
    
    def getInstructionMemory(self):
        return self.__instructionMemory
    
    def getLabelMap(self):
        return self.__labelMap