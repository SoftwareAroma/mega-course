from functools import wraps


def bold(func):
    """This is the wrapper function"""

    @wraps(func)
    def wrapper():
        return f'<b>{func()}</b>'

    return wrapper


def italics(func):
    """This is the wrapper function"""

    @wraps(func)
    def wrapper():
        return f'<i>{func()}</i>'

    return wrapper


@bold
@italics
def print_fib():
    """return Fibonacci"""
    return 'Fibonacci'


print(print_fib())
