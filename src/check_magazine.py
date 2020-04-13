from collections import Counter


def check_magazine(magazine, note):
    magazine_tokens = Counter(magazine)
    note_tokens = Counter(note)
    for token in note_tokens:
        if note_tokens[token] > magazine_tokens[token]:
            return "No"

    return "Yes"
