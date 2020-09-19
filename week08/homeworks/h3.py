"""Timer decorator"""
import time
import functools


def timer(func):
    """A timer decorator"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'{func.__name__} took {(end - start) * 1000} ms')
        return res
    return wrapper


class Timer:
    def __init__(self):
       pass

    def __call__(self, func):
        """Class decorator"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("In call")
            start = time.perf_counter()
            res = func(*args, **kwargs)
            end = time.perf_counter()
            print(f'{func.__name__} took {(end - start) * 1000} ms')
            return res
        print("After call")
        return wrapper

#@timer
@Timer()
def fib(n):
    memo = {}
    def helper(n):
        if n <= 2: return n
        if n in memo:
            return memo[n]
        memo[n] = helper(n - 1) + helper(n - 2)
        return memo[n]
    return helper(n)


if __name__ == '__main__':
    print(fib(16))