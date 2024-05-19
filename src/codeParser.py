import src.grammar as grammar
from src.codeFile import CodeFile

class CodeParser:
    def __init__(self, code: CodeFile):
        """
        code: CodeFile -> None

        Constructor for the code parser class
        """

        self.__code = code
        self.__parsedCode = []
        for line in self.__code.code:
            tree = self.__parseLine(line)
            self.__parsedCode.append(tree)
        
        self.__code.importSyntaxTrees(self.__parsedCode)

    def getCode(self):
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
        tree = grammar.parse(line, rules[0].left, rules, False)
        
        if tree is None:
            raise SyntaxError("Failed to parse line: " + line)
        
        return tree