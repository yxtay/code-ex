def get_ways(n, c):
    # Write your code here
    if n == 0:
        return 1
    elif n > 0 and len(c) == 0:
        return 0
    else:
        val = c[-1]
        n_ways = n // val + 1
        return sum(get_ways(n - val * i, c[:-1]) for i in range(n_ways))


def get_ways_memo(n, c, memo=None):
    if memo is None:
        memo = {}

    key = (n, len(c))
    if key in memo:
        return memo[key]
    # Write your code here
    if n == 0:
        result = 1
    elif n > 0 and len(c) == 0:
        result = 0
    else:
        val = c[-1]
        n_ways = n // val + 1
        result = sum(get_ways_memo(n - val * i, c[:-1], memo) for i in range(n_ways))

    memo[key] = result
    return result


def get_ways_dp(n, c):
    len_c = len(c)
    dp = [[0] * len_c for _ in range(n + 1)]
    # row: value remaining
    # col: coin value

    # if value remaining == 0
    # valid solution, hence fill count = 1
    for col in range(len_c):
        dp[0][col] = 1

    for row in range(1, n + 1):
        for col in range(len_c):
            # count number of solution deducting coin value
            x = dp[row - c[col]][col] if row >= c[col] else 0

            # count number of solutions without using coin
            y = dp[row][col - 1]

            dp[row][col] = x + y

    return dp[n][len_c - 1]
