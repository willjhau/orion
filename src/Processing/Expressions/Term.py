from . import Factor
from ...LangData.oDataTypes import oFloat

def evaluateTerm(ctx, term):
    if len(term.children) == 1:
        return Factor.evaluateFactor(ctx, term.children[0])
    else:
        left = Factor.evaluateFactor(ctx, term.children[0])
        right = evaluateTerm(ctx, term.children[2])
        if term.children[1].symbol.name == '*':
            return oFloat(left * right)
        else:
            return oFloat(left / right)
