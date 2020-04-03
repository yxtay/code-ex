def minion_game(string):
    # your code goes here
    stuart = 0
    kevin = 0
    vowels = set("AEIOU")
    for i, ch in enumerate(string):
        if ch in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i

    if kevin > stuart:
        return "KEVIN", kevin
    elif stuart > kevin:
        return "STUART", stuart
    else:
        return "DRAW", stuart
