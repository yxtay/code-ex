def is_balanced(s):
    pairs = {"(": ")", "[": "]", "{": "}"}

    stack = []
    for ch in s:
        if ch in pairs:
            stack.append(ch)
        else:
            if len(stack) == 0:
                return False

            if pairs[stack.pop()] != ch:
                return False
    return len(stack) == 0
