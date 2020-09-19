"""Implementation of map func"""
def map(func, lst, *lsts):
    for args in zip(lst, *lsts):
        # single star * unpacks the sequence/collection into positional arguments
        yield func(*args)


def time2(x, y):
    return x*y


if __name__ == '__main__':
    print(list(map(time2, range(1, 4), range(4, 9))))