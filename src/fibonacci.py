import functools


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


@functools.lru_cache(maxsize=128)
def fibonacci_lru(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print(n)
        return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)


def memoize(func):
    memory = {}

    @functools.wraps(func)
    def memoized_func(n):
        if n not in memory:
            memory[n] = func(n)
        return memory[n]

    return memoized_func


fibonacci_mem = memoize(fibonacci)
fibonacci_cache = functools.lru_cache(maxsize=128)(fibonacci)
