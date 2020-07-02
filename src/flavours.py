def what_flavours(cost, money):
    remaining = {}
    for i, el in enumerate(cost):
        if el in remaining:
            return remaining[el], i + 1

        remaining[money - el] = i + 1
