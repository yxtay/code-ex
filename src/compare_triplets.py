def compare_triplets(a, b):
    scores = [0, 0]
    for i, j in zip(a, b):
        if i > j:
            scores[0] += 1
        elif i < j:
            scores[1] += 1
        else:
            pass
    return scores
