from collections import Counter


def freq_query(queries):
    int_count = Counter()
    freq_count = Counter()
    output = []
    for op, n in queries:
        if op == 1:
            if freq_count[int_count[n]] > 0:
                freq_count[int_count[n]] -= 1
            int_count[n] += 1
            freq_count[int_count[n]] += 1
        elif op == 2:
            if int_count[n] > 0:
                freq_count[int_count[n]] -= 1
                int_count[n] -= 1
                freq_count[int_count[n]] += 1
        elif op == 3:
            output.append(1 if freq_count[n] > 0 else 0)
    return output
