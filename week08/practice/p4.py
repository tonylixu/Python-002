# k = lambda x:x+1
def k(x): return x + 1

print(k(1))


def square(x):
    return x**2


m = map(square, range(10))
print(m)
print(next(m))
print(next(m))
print(dir(m))