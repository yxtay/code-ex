def minimum_bribes(q):
    q = [p - 1 for p in q]

    bribes = 0
    for i, p in enumerate(q):
        if p - i > 2:
            return None

        for j in range(max(p-1, 0), i):
            if q[j] > p:
                bribes += 1

    return bribes
