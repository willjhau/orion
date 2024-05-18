from Grammar import grammar
from Grammar import SyntaxTree

class CodeFile:
    def __init__(self):
        """
        path: str -> None

        Constructor for the code file class. Initialises the path and the code
        """

        self.path = None
        self.code = None
        self.codeTrees = None

    def readFromFile(self, path):
        """
        path: str -> None

        Reads the code from a file
        """

        with open(path, 'r') as file:
            self.code = file.readlines()
            self.path = path
        
    def importSyntaxTrees(self, codeTrees):
        """
        codeTrees: SyntaxTree[] -> None

        Imports the syntax trees
        """

        if len(self.codeTrees) != len(self.code):
            raise SyntaxError("Code and syntax trees are not the same length")
    
        self.codeTrees = codeTrees

    def importFromList(self, code):
        """
        code: str[] -> None

        Imports the code from a list
        """
        self.path = None
        self.code = code
        
    def getLine(self, lineNumber):
        """
        lineNumber: int -> str

        Returns the line of code at the specified line number
        """

        return self.code[lineNumber]
    
    def getLineCount(self):
        """
        None -> int

        Returns the number of lines in the code
        """

        return len(self.code)
    
    def getLines(self):
        """
        None -> str[]

        Returns all the lines of code
        """

        return self.code
    
    def getPath(self):
        """
        None -> str

        Returns the path of the file
        """

        return self.path    
    
