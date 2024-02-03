def cleaner(symbolsToDelete: list):
    """
    Helper function that call the garbage collector (clean the symbol's mess).
    """
    try:
        for z0 in symbolsToDelete:
            del globals()[z0]
    except KeyError:
        print("Symbolic variables already cleared")