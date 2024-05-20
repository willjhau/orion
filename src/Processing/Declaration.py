from ..LangData.oDataTypes import *
from ..LangData.oDataStructures import oArray
from .Expression import evaluateExpression

def executeDeclaration(ctx, DeclarationNode):
    if len(DeclarationNode.children) == 2:
        oType = DeclarationNode.children[0].symbol.matched_string
        name = DeclarationNode.children[1].matched_string
        if oType == "int":
            ctx.getDataMap()[name] = oInt(None)
            return
        if oType == "float":
            ctx.getDataMap()[name] = oFloat(None)
            return
        if oType == "boolean":
            ctx.getDataMap()[name] = oBool(None)
            return
        if oType == "char":
            ctx.getDataMap()[name] = oChar(None)
            return
        if oType == "String":
            ctx.getDataMap()[name] = oString(None)
            return
        if oType == "Array":
            raise Exception("Array declaration must include size")
        
    if len(DeclarationNode.children) == 3: # Form Type name Expression
        oType = DeclarationNode.children[0].symbol.matched_string
        name = DeclarationNode.children[1].matched_string
        value = evaluateExpression(DeclarationNode.children[2])

        if oType == "int":
            if not oInt.isValid(value):
                raise Exception("Invalid value for int declaration")
            ctx.getDataMap()[name] = oInt(value)
            return
        if oType == "float":
            if not oFloat.isValid(value):
                raise Exception("Invalid value for float declaration")
            ctx.getDataMap()[name] = oFloat(value)
            return
        if oType == "boolean":
            if not oBool.isValid(value):
                raise Exception("Invalid value for boolean declaration")
            ctx.getDataMap()[name] = oBool(value)
            return
        if oType == "char":
            if not oChar.isValid(value):
                raise Exception("Invalid value for char declaration")
            ctx.getDataMap()[name] = oChar(value)
            return
        if oType == "String":
            if not oString.isValid(value):
                raise Exception("Invalid value for String declaration")
            ctx.getDataMap()[name] = oString(value)
            return
        if oType == "Array":
            if not isinstance(value, oArray):
                raise Exception("Invalid value for Array declaration")
            ctx.getDataMap()[name] = value
            return
    raise Exception("Invalid declaration syntax")

    pass