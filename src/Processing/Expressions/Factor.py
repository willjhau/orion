from . import Literal
from .. import FunctionCall
from . import ArrayAccess
from . import FloatLiteral
from . import IntegerLiteral
from .. import Expression
from ...LangData.oDataTypes import oFloat, oInt

def evaluateFactor(ctx, factor):
    if len(factor.children) == 1:
        if factor.children[0].symbol.name == "Literal":
            return Literal.evaluateLiteral(ctx, factor.children[0])
        
        if factor.children[0].symbol.name == 'FunctionCall':
            return FunctionCall.executeFunction(ctx, factor.children[0])
        
        if factor.children[0].symbol.name == 'ArrayAccess':
            return ArrayAccess.evaluate(ctx, factor.children[0])
        
        if factor.children[0].symbol.name == 'Identifier':
            return ctx.getDataMap().getData(factor.children[0].matched_string)
        
    if len(factor.children) == 2:
        if factor.children[1].symbol.name == "FloatLiteral":
            return oFloat(-1* FloatLiteral.evaluate(ctx, factor.children[1]).getValue())
        
        if factor.children[1].symbol.name == "IntegerLiteral":
            return oInt(-1 * IntegerLiteral.evaluate(ctx, factor.children[1]).getValue())
        
    if len(factor.children) == 3:
        return Expression.evaluateExpression(ctx, factor.children[1])
        

        
