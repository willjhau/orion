from ..LangData.oDataTypes import *
from ..LangData.oDataStructures import oArray
from .Expression import evaluateExpression

def executeDeclaration(ctx, DeclarationNode):
    if len(DeclarationNode.children) == 2:
        oType = DeclarationNode.children[0].matched_string
        name = DeclarationNode.children[1].matched_string
        if oType == "int":
            ctx.getDataMap().addData(name, oInt, oInt(None))
            return
        if oType == "float":
            ctx.getDataMap().addData(name, oFloat, oFloat(None))
            return
        if oType == "boolean":
            ctx.getDataMap().addData(name, oBool, oBool(None))
            return
        if oType == "char":
            ctx.getDataMap().addData(name, oChar, oChar(None))
            return
        if oType == "String":
            ctx.getDataMap().addData(name, oString, oString(None))
            return
        if oType == "Array":
            raise Exception("Array declaration must include size")
        
    if len(DeclarationNode.children) == 3: # Form Type name Expression
        oType = DeclarationNode.children[0].matched_string
        name = DeclarationNode.children[1].matched_string
        value = evaluateExpression(ctx, DeclarationNode.children[2])

        if oType == "int":
            if not oInt.isValid(value.getValue()):
                raise Exception("Invalid value for int declaration")
            ctx.getDataMap().addData(name, oInt, value)
            return
        if oType == "float":
            if not oFloat.isValid(value):
                raise Exception("Invalid value for float declaration")
            ctx.getDataMap().addData(name, oFloat, value)
            return
        if oType == "boolean":
            if not oBool.isValid(value):
                raise Exception("Invalid value for boolean declaration")
            ctx.getDataMap().addData(name, oBool, value)
            return
        if oType == "char":
            if not oChar.isValid(value):
                raise Exception("Invalid value for char declaration")
            ctx.getDataMap().addData(name, oChar, value)
            return
        if oType == "String":
            if not oString.isValid(value):
                raise Exception("Invalid value for String declaration")
            ctx.getDataMap().addData(name, oString, value)
            return
        if oType == "Array":
            if not isinstance(value, oArray):
                raise Exception("Invalid value for Array declaration")
            ctx.getDataMap().addData(name, oArray, value)
            return
    raise Exception("Invalid declaration syntax")

    pass