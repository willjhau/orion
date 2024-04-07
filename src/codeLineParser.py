from instructionMemory import InstructionMemory
from labelMap import LabelMap
from specialCharacters import SpecialCharacters

class Parser:
    """
    Converts the source code into instruction memory and label map
    """
    def __init__(self, path: str):
        """
        path: str -> None

        Constructor for the parser class. Initialises instruction memory and label map
        """

        self.path = path
        self.instructionMemory = InstructionMemory(None)
        self.labelMap = LabelMap()
        self.__characterSet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-=/.\'\"%^*()[]<>#_;"

    def __getNextElement(self, line: str, array = False):
        """
        line: str -> str

        Reads a line of orion code and returns the first item
        """

        output = ""

        if array:
            if line[0] == SpecialCharacters.ARGUMENT_SEPARATOR:
                return output
            if line[0] == '\"':
                output += line[0]
                line = line[1:]
                while len(line) != 0:
                    if line[0] == '\"':
                        output += line[0]
                        return output
                    output += line[0]
                    line = line[1:]
                raise SyntaxError("String not terminated")
            
    def __getStringCharacterMap(self, line: str):
        """
        line: str -> Tuple[](chr, boolean)

        Converts a line into a mapping of whether each character is part of a valid string
        """
        stringCharacterMap = [False for char in line] # Stores a list of characters and whether they are part of a string

        isString = False

        i = 0
        while i < len(line):
            char = line[i]

            if char == SpecialCharacters.ESCAPE_CHARACTER:
                if not isString:
                    raise SyntaxError("Cannot escape string when escape character is not part of a string")

                stringCharacterMap[i] = True
                if (i + 1) < len(line):
                    stringCharacterMap[i+1] = True
                
                i = i + 2
                continue
                    
            if char == SpecialCharacters.STRING_MARKER:
                stringCharacterMap[i] = True
                if isString:
                    isString = False
                else:
                    isString = True
            else:
                stringCharacterMap[i] = isString
            

            i = i + 1

        return zip(line, stringCharacterMap)    
    
    def __removeComment(self, line):
        """
        line: str -> str

        Reads a line of orion code and removes a comment. Returns the same line without the comment
        """

        strippedLine = ""

        stringCharacterMap = self.__getStringCharacterMap(line)

        for char, isString in stringCharacterMap:
            if char == SpecialCharacters.COMMENT_MARKER and (not isString):
                return strippedLine
            
            strippedLine += char

        return strippedLine

    
if __name__ == "__main__":

    parser = Parser("dummy")

    print(parser.removeComment("abcdef\"ghi#testjkl\"mn#testop\"qrs\\\"tuv\"wxyz#test"))



        




