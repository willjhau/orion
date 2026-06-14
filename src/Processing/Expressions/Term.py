from . import Factor
from ...LangData.oDataTypes import oFloat, oInt

def evaluateTerm(ctx, term):
    if len(term.children) == 1:
        return Factor.evaluateFactor(ctx, term.children[0])

    left  = Factor.evaluateFactor(ctx, term.children[0])
    right = evaluateTerm(ctx, term.children[2])
    lv = left.getValue()
    rv = right.getValue()

    if term.children[1].matched_string == '*':
        if isinstance(lv, int) and isinstance(rv, int) \
                and not isinstance(lv, bool) and not isinstance(rv, bool):
            return oInt(lv * rv)
        return oFloat(float(lv) * float(rv))

    # Division: integer / integer with no remainder stays integer.
    if isinstance(lv, int) and isinstance(rv, int) \
            and not isinstance(lv, bool) and not isinstance(rv, bool):
        if rv == 0:
            raise ZeroDivisionError("Integer division by zero")
        if lv % rv == 0:
            return oInt(lv // rv)
    return oFloat(float(lv) / float(rv))
