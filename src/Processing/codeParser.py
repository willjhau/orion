from ..Grammar.grammar import parseLine
from ..Structures.codeFile import CodeFile

class CodeParser:
    def __init__(self, code: CodeFile):
        self.__code = code
        self.__parsedCode = []
        for line in code.getCode():
            tree = parseLine(line)
            self.__parsedCode.append(tree)
        self.__code.importSyntaxTrees(self.__parsedCode)

    def getCodeFile(self):
        return self.__code
