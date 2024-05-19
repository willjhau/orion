from . import Factor

def evaluateTerm(ctx, term):
    if len(term.children) == 1:
        return Factor.evaluateFactor(ctx, term.children[0])
    else:
        left = Factor.evaluateFactor(ctx, term.children[0])
        right = evaluateTerm(ctx, term.children[2])
        if term.children[1].symbol.name == '*':
            return left * right
        else:
            return left / right