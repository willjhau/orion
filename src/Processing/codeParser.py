from ..Grammar import grammar as grammar
from ..Structures.codeFile import CodeFile

class CodeParser:
    def __init__(self, code: CodeFile):
        """
        code: CodeFile -> None

        Constructor for the code parser class
        """

        self.__code = code
        self.__parsedCode = []
        for line in code.getCode():
            tree = self.__parseLine(line)
            if tree == {}:
                raise SyntaxError("Failed to parse line: " + line)
            self.__parsedCode.append(tree)
        
        self.__code.importSyntaxTrees(self.__parsedCode)

    def getCodeFile(self):
        """
        None -> CodeFile

        Returns the code
        """

        return self.__code
    
    def __parseLine(self, line: str):
        """
        line: str -> SyntaxTree

        Parses a line of code
        """
        rules = grammar.readGrammar('src/Grammar/grammar.txt', line)
        tree = grammar.parse(line, rules[0].left, rules, False).tidyTree()

        
        if tree is None:
            raise SyntaxError("Failed to parse line: " + line)
        
        return tree