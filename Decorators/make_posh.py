# import the func tools
from functools import wraps


def make_posh(func):
    """This is the wrapper function"""

    @wraps(func)
    def wrapper():
        output = f'''
        +---------+
        |         |
        {func()} 
        |         |
        +=========+   
        '''
        return output

    # for debugging  (manual way)
    # wrapper.__name__ = func.__name__
    # wrapper.__doc__ = func.__doc__

    return wrapper


@make_posh
def print_fib():
    """Print out Fibonacci"""
    return ' Fibonacci '


print(print_fib())
