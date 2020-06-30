def super_digit(n, k=1):
    if len(n) == 1:
        if k == 1:
            return int(n)
        else:
            return super_digit(str(int(n) * k))
    else:
        return super_digit(str(sum(int(digit) for digit in n)), k)
