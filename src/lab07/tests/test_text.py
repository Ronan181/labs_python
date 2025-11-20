import pytest
import sys
import os

sys.path.append("/Users/ars/Documents/GitHub/labs_python/src/lib/")
from text import *

# normalize


@pytest.mark.parametrize(
    "text, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
    ],
)
def test_normalize(text, expected):
    assert normalize(text) == expected


# tokenize


@pytest.mark.parametrize(
    "text, expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
        ("", []),
    ],
)
def test_tokenize(text, expected):
    assert tokenize(text) == expected


# count_freq


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["a", "b", "a", "c", "b", "a"], {"a": 3, "b": 2, "c": 1}),
        (["bb", "aa", "bb", "aa", "cc"], {"aa": 2, "bb": 2, "cc": 1}),
        ([], {}),
    ],
)
def test_count_freq(tokens, expected):
    assert count_freq(tokens) == expected


# top_n


@pytest.mark.parametrize(
    "freq, n, expected",
    [
        ({"a": 3, "b": 2, "c": 1}, 2, [("a", 3), ("b", 2)]),
        ({"aa": 2, "bb": 2, "cc": 1}, 2, [("aa", 2), ("bb", 2)]),
        ({}, 5, []),
        ({"a": 3}, 0, []),
        ({"a": 3, "b": 2}, 10, [("a", 3), ("b", 2)]),
    ],
)
def test_top_n(freq, n, expected):
    assert top_n(freq, n) == expected


# black src/lab07/tests/test_text.py
# black src/lab07/tests/test_json_csv.py
# pytest src/lab07/tests/test_text.py -v
# pytest src/lab07/tests/test_json_csv.py -v

