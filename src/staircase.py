def staircase(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    steps = [1, 2, 3]
    if n < 0:
        result = 0
    elif n == 0:
        result = 1
    else:
        result = sum(staircase(n - step) for step in steps)
    memo[n] = result
    return result
