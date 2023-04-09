import functools


def persistence(n):
    times = 0

    while n > 9:
        n = functools.reduce(lambda x, y: x * y, [int(i) for i in str(n)])
        times += 1

    return times