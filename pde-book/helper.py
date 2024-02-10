from sympy import Eq


def cleaner(symbolsToDelete: list):
    """
    Helper function that call the garbage collector (clean the symbol's mess).
    """
    try:
        for z0 in symbolsToDelete:
            del globals()[z0]
    except KeyError:
        print("Symbolic variables already cleared")


class Approx(Eq):
    def _latex(self, printer):
        return rf"{printer._print(self.lhs)} \approx {printer._print(self.rhs)}"
