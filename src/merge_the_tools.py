def merge_the_tools(string, k):
    # your code goes here
    substrings = []
    for i in range(len(string) // k):
        substrings.append(reduced_str(string[i * k : (i + 1) * k]))
    print("\n".join(substrings))
    return substrings


def reduced_str(string):
    reduced = ""
    for ch in string:
        if ch not in reduced:
            reduced += ch
    return reduced
