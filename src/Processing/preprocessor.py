from ..Structures.codeFile import CodeFile
from ..LangData.exceptions import *
from ..LangData.specialCharacters import SpecialCharacters

class Preprocessor:
    def __init__(self, code: CodeFile):
        """
        code: CodeFile -> None

        Constructor for the preprocessor class
        """
        self.__code = code
        self.__processedCode = []
        self.__preprocess()
        self.__code.importFromList(self.__processedCode)
    
    def getCode(self):
        """
        None -> CodeFile

        Returns the code
        """

        return self.__code

    def __checkIllegalCharacters(self, line: str):
        """
        line: str -> True

        Reads a line of orion code and checks for any illegal characters, returning True if there are none
        """

        stringCharacterMap = self.__getStringCharacterMap(line)

        for char, isString in stringCharacterMap:
            if not isString and char not in SpecialCharacters.ALLOWED_CHARACTERS:
                raise SyntaxError("Illegal character found in line: " + line + str(ord(char)) + " (" + char + ")")
            
        return True

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
    
    def __removeWhitespace(self, line):
        """
        line: str -> str

        Reads a line of orion code and removes whitespace. Returns the same line where all 
        trailing and leading whitespace has been removed. Also all whitespace between characters
        which are not part of a string are compressed to a single space. Line breaks are also removed.
        """

        strippedLine = ""

        stringCharacterMap = self.__getStringCharacterMap(line)

        for char, isString in stringCharacterMap:
            if char == " " and not isString:
                if strippedLine == "":
                    continue
                if strippedLine[-1] == " ":
                    continue
                strippedLine += " "
            else:
                strippedLine += char
        if strippedLine.endswith("\n"):
            strippedLine = strippedLine[:-1]
        return strippedLine
    

    def __preprocess(self):
        """
        None -> None

        Preprocesses the code and returns
        """

        for line in self.__code.getLines():
            lineNoComment = self.__removeComment(line)

            if not self.__checkIllegalCharacters(lineNoComment):
                continue
    
            if line == "":
                continue
            
            lineNoWhitespace = self.__removeWhitespace(lineNoComment)

            if lineNoWhitespace == "":
                continue

            self.__processedCode.append(lineNoWhitespace)
        
    def getProcessedCode(self):
        """
        None -> str[]

        Returns the processed code
        """

        return self.__processedCode


