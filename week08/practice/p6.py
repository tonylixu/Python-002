def outer(func):
    def inner(a, b):
        print(f'inner: {func.__name__}')
        print(a, b)
        func(a, b)
    return inner


@outer
def foo(a, b):
    print(a+b)
    print(f'foo {foo.__name__}')

foo(1, 2)
# inner:
# 1, 2
# 3
# foo


def outer3(func):
    def inner3(*args, **kwargs):
        ret = func(*args, **kwargs)
        return ret
    return inner3


@outer3
def foo3(a, b, c):
    print(foo3.__name__)
    return a + b + c

print(foo3(1, 2, 3))


# Decorator with parameters
def outer_arg(bar):
    def outer(func):
        def inner(*args, **kwargs):
            ret = func(*args, **kwargs)
            print(bar)
            return ret
        return inner
    return outer


@outer_arg('foo_arg')
def foo(a, b, c):
    return a + b + c

print(foo(3, 4, 5))