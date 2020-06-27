def get_minimum_cost(friends, flowers):
    total = 0
    for i, cost in enumerate(sorted(flowers, reverse=True)):
        total += (1 + i // friends) * cost
    return total
