import pytest

from src.check_magazine import check_magazine

cases = [
    (["give", "me", "one", "grand", "today", "night"], ["give", "one", "grand", "today"], "Yes"),
    (["two", "times", "three", "is", "not", "four"], ["two", "times", "two", "is", "four"], "No"),
    (
        ["ive", "got", "a", "lovely", "bunch", "of", "coconuts"],
        ["ive", "got", "some", "coconuts"],
        "No",
    ),
]


@pytest.mark.parametrize("magazine, note, expected", cases)
def test(magazine, note, expected):
    result = check_magazine(magazine, note)
    assert result == expected
