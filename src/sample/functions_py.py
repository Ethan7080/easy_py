def p(*args, **kwargs):
    """
    Shorthand function for the print function.
    """
    print(*args, **kwargs)

def i(value, *args, **kwargs):
    """
    Shorthand function for the int function.
    """
    
    return int(value, *args, **kwargs)

def l(string, *args, **kwargs):
    """
    Shorthand function for the len function
    """
    return len(string)

def t(objects, *args, **kwargs):
    """
    Shorthand function for the type function
    """
    return type(objects)

def st(value, *args, **kwargs):
    """
    Shorthand function for the str function
    """
    return str(value)
def f(value, *args, **kwargs):
    """
    Shorthand function for the float function
    """
    return float(value)

def l(iterable):
    """
    Shorthand function for the list conversion.
    """
    return list(iterable)
def d(*args, **kwargs):
    """
    Shorthand function for the dict constructor.
    """
    return dict(*args, **kwargs)

def t(iterable):
    """
    Shorthand function for the tuple constructor.
    """
    return tuple(iterable)

def s(iterable):
    """
    Shorthand function for the set constructor.
    """
    return set(iterable)