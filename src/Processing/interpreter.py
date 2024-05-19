from FunctionCall import executeFunction
from Declaration import Declaration
from Assignment import Assignment
from Expression import Expression

class Context:
    def __init__(self, instructionMemory, labelMap):
        self.__instructionMemory = instructionMemory
        self.__labelMap = labelMap
        self.__dataMap = {}

    def getInstructionMemory(self):
        return self.__instructionMemory
    
    def getLabelMap(self):
        return self.__labelMap
    
    def getDataMap(self):
        return self.__dataMap

class Interpreter:
    def __init__(self, instructionMemory, labelMap):
        self.context = Context(instructionMemory, labelMap)

    def argTreeToArgList(self, functionCallNode):
        print(functionCallNode.children)
        if len(functionCallNode.children) == 0:
            return []
        if len(functionCallNode.children) == 1:
            return [functionCallNode.children[0]]
        return [functionCallNode.children[0]] + self.argTreeToArgList(functionCallNode.children[1])

    def executeNext(self):
        instruction = self.__instructionMemory.getCurrentInstruction()

        if instruction.children[0].symbol.name == "FunctionCall":
            return executeFunction(self.context, instruction.children[0].symbol.name, self.argTreeToArgList(instruction.children[0]))
        

        elif instruction.children[0].symbol.name == "Declaration":
            # TODO
            pass

        elif instruction.children[0].symbol.name == "Assignment":
            # TODO
            pass

        elif instruction.children[0].symbol.name == "Expression":
            # TODO
            pass