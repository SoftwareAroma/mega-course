# # # python decorators

def my_decorator(func):
    """Decorator function"""

    def wrapper():
        """return string F-I-B-O-N-A-C-C-I"""
        return 'F-I-B-O-N-A-C-C-I'

    return wrapper


@my_decorator
def p_fib():
    """Print out Fibonacci"""
    return 'Fibonacci'


# p_fib = my_decorator(p_fib)
print(p_fib())
