def print_fib(a, *args):
    print(a)
    print(args)


def print_fi(**kwargs):
    print(kwargs)


def p_fib(*args, **kwargs):
    print(args)
    print(kwargs)


print_fib("first", 1, 2, 4)
print("\n")
print_fi(fi=1, se=2, th=3, fo=4)
print("\n")
p_fib(6, 7, 8, 9, fi=1, se=2, th=3, fo=4)
