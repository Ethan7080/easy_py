import importlib

print('Welcome to easy_py!!!   :D')


def p(param: str) -> None:
    """
    Short print function
    :param param:
    :return:
    """
    print(param)


def add(*nums: int) -> int:
    """
    Easy add function
    :param nums:
    :return:
    """
    return sum(nums)


def i(string: str) -> int:
    """
    Short int function
    :param string:
    :return:
    """
    return int(string)


def s(num: int) -> str:
    """
    Short string function
    :param num:
    :return:
    """
    return str(num)


def im(modules: list) -> None:
    """
    Short import function
    :param modules:
    :return:
    """
    for module in modules:
        globals()[module] = importlib.import_module(module)


def l(string: str) -> int:
    """
    Short len function
    :param string:
    :return:
    """
    return len(string)
