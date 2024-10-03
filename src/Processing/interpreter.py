from .FunctionCall import executeFunction
from .Declaration import executeDeclaration
from .Assignment import executeAssignment
from ..Structures import dataMap
# from .Expression import Expression

class Context:
    def __init__(self, instructionMemory, labelMap):
        self.__instructionMemory = instructionMemory
        self.__labelMap = labelMap
        self.__dataMap = dataMap.DataMap()

    def getInstructionMemory(self):
        return self.__instructionMemory
    
    def getLabelMap(self):
        return self.__labelMap
    
    def getDataMap(self):
        return self.__dataMap

class Interpreter:
    def __init__(self, instructionMemory, labelMap):
        self.context = Context(instructionMemory, labelMap)

    def run(self):
        while True:
            self.executeNext()

    def argTreeToArgList(self, functionCallNode):
        if len(functionCallNode.children) == 0:
            return []
        if len(functionCallNode.children) == 1:
            return [functionCallNode.children[0]]
        return [functionCallNode.children[0]] + self.argTreeToArgList(functionCallNode.children[1])

    def executeNext(self):
        instruction = self.context.getInstructionMemory().getCurrentInstruction()
        self.context.getInstructionMemory().incrementCounter()

        if instruction.children[0].symbol.name == "FunctionCall":
            executeFunction(self.context, instruction.children[0])
        elif instruction.children[0].symbol.name == "Declaration":
            return executeDeclaration(self.context, instruction.children[0])

        elif instruction.children[0].symbol.name == "Assignment":
            return executeAssignment(self.context, instruction.children[0])

        elif instruction.children[0].symbol.name == "Expression":
            # TODO
            pass