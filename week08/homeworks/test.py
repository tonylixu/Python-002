from functools import wraps
import time

class MyClass:
    def __init__(self):
         #   var='init_var',
         #   *args,
         #   **kwargs):
        #self._v = var
        #super(MyClass, self).__init__(*args, **kwargs)
        pass

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            start = time.perf_counter()
            func_name = func.__name__ + ' was called'
            ret = func(*args, **kwargs)
            end = time.perf_counter()
            print(f'{func.__name__} took {(end - start) * 1000} ms')
            return ret
        return wrapped_function

@MyClass()
def myfunc(a):
    print(myfunc.__name__)
    pass

myfunc(3)