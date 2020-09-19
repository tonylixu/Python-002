def counter(start=0):
    count = [start]

    def incr():
        count[0] += 1
        return count[0]
    return incr

c1 = counter(10)
print(c1.__code__.co_freevars)