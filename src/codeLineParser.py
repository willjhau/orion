from src.instructionMemory import InstructionMemory
from src.labelMap import LabelMap

class Parser:
    """
    Converts the source code into instruction memory and label map
    """
    def __init__(self, path):
        """
        path: str -> None

        Constructor for the parser class. Initialises instruction memory and label map
        """

        self.path = path
        self.instructionMemory = InstructionMemory()
        self.labelMap = LabelMap()
        self.__characterSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-=/.\'\"%^*()[]<>#_;"
    
    def __stripCodeLine(self, line):
        """
        line: str -> str

        Converts a line of orion code into a standardised format
        """
        outputLine = ""

        # Stage 1, remove leading and trailing whitespace
        line = line.strip()

        # Loop while the string is not empty
        while len(line) > 0:
            argument = ""

            isString = False
            # Build the string containing the current argument
            while len(line) > 0:
                # If the argument is a string literal, accept any character
                if isString:
                    if line[0] == '\"':
                        isString = not isString
                    
                    argument += line[0]
                    line = line[1:]
                    continue

                # Check if the character is a string constructor
                if line[0] == '\"':
                    isString = not isString
                # Check if the character initialises a comment
                if line[0] == '#' and not isString:
                    outputLine += argument;

                argument += line[0]
                line = line[1:]
            
            outputLine += argument
            outputLine += " "

            line = line.strip()
        
        outputLine.strip()

        self.instructionMemory.addInstruction(outputLine)
        




