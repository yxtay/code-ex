def abbreviation(a, b):
    if len(b) == 0:
        return a.lower() == a
    elif len(a) < len(b):
        return False
    elif a[0] == b[0]:
        # a_ch and b_ch match
        return abbreviation(a[1:], b[1:])
    elif a[0].isupper():
        # a_ch and b_ch do not match, a_ch is upper case
        return False
    elif a[0].upper() == b[0]:
        # a_ch is lower case and upper case matches b_ch
        return abbreviation(a[1:], b[1:]) or abbreviation(a[1:], b)
    else:
        # a_ch is lower case and upper case do not match b_ch
        return abbreviation(a[1:], b)


def abbreviation_dp(a, b):
    m, n = len(a), len(b)
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    # when both are empty strings, it is definitely true
    dp[0][0] = True
    # when b is empty string, row = 0
    # check if a is lower case, which can be dropped
    # previous sub problem is col - 1
    for col in range(1, m + 1):
        dp[0][col] = a[col - 1].islower() and dp[0][col - 1]
    # when a is empty string, col = 0
    # always false, no need to check
    # since matrix initialised with false, no further action

    for row in range(1, n + 1):
        for col in range(1, m + 1):
            if dp[row - 1][col - 1] and a[col - 1].upper() == b[row - 1]:
                # a_ch and b_ch match, remove both
                # sub problem: row - 1, col - 1
                dp[row][col] = True
                continue

            if dp[row][col - 1] and a[col - 1].islower():
                # a_ch is lower case, can be dropped
                # sub problem: row, col - 1
                dp[row][col] = True
            # else cell remain false, no action required
    return dp[n][m]
