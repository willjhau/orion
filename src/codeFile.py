from src.Grammar import grammar
from src.Grammar import SyntaxTree

class CodeFile:
    def __init__(self):
        """
        path: str -> None

        Constructor for the code file class. Initialises the path and the code
        """

        self.__path = None
        self.__code = None
        self.__codeTrees = None

    def readFromFile(self, path):
        """
        path: str -> None

        Reads the code from a file
        """

        with open(path, 'r') as file:
            self.__code = file.readlines()
            self.__path = path
        
    def importSyntaxTrees(self, codeTrees):
        """
        codeTrees: SyntaxTree[] -> None

        Imports the syntax trees
        """

        if len(self.getCodeTrees()) != len(self.getLines()):
            raise SyntaxError("Code and syntax trees are not the same length")
    
        self.__codeTrees = codeTrees

    def importFromList(self, code):
        """
        code: str[] -> None

        Imports the code from a list
        """
        self.__code = code

    def getLineTree(self, lineNumber):
        """
        lineNumber: int -> SyntaxTree

        Returns the syntax tree at the specified line number
        """

        return self.__codeTrees[lineNumber]

    def setPath(self, path):
        """
        path: str -> None

        Sets the path of the file
        """

        self.__path = path
        
    def getLine(self, lineNumber):
        """
        lineNumber: int -> str

        Returns the line of code at the specified line number
        """

        return self.__code[lineNumber]
    
    def getLineCount(self):
        """
        None -> int

        Returns the number of lines in the code
        """

        return len(self.__code)
    
    def getLines(self):
        """
        None -> str[]

        Returns all the lines of code
        """

        return self.__code
    
    def getCodeTrees(self):
        """
        None -> SyntaxTree[]

        Returns the syntax trees
        """

        return self.__codeTrees
    
    def getPath(self):
        """
        None -> str

        Returns the path of the file
        """

        return self.__path    
    
