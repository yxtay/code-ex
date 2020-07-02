def pairs(k, arr):
    return len(set(arr) & set(el + k for el in arr))
