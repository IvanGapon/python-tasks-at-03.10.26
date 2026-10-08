import pytest

from task_500_keyboard_row.solution_500 import Solution


@pytest.fixture
def solver():
    return Solution()


@pytest.mark.parametrize(
    "words, expected",
    [
        # --- Базовые примеры из задачи ---
        (["Hello", "Alaska", "Dad", "Peace"], ["Alaska", "Dad"]),
        (["omk"], []),
        (["adsdf", "sddfd"], ["adsdf", "sddfd"]),

        # --- Регистр букв ---
        (["A", "b", "z"], ["A", "b", "z"]),
        (["aLaSkA", "PEACE", "DAD"], ["aLaSkA", "DAD"]),
        (["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"], ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]),

        # --- Однобуквенные слова ---
        (["q", "w", "e", "a", "s", "z", "x"], ["q", "w", "e", "a", "s", "z", "x"]),

        # --- Граничные случаи ---
        ([], []),
        (["a", "bc", "def"], ["a", "bc"]),
        (["qwerty", "asdf", "zxcv", "qwertyz"], ["qwerty", "asdf", "zxcv"]),

        # --- Повторяющиеся символы ---
        (["lllllllll", "qqqqqqqqq", "zzzzzzzzz"], ["lllllllll", "qqqqqqqqq", "zzzzzzzzz"]),
        (["AlAsKaA", "DaDdY"], ["AlAsKaA"]),
    ],
)
def test_find_words(solver, words: list[str], expected: list[str]):
    assert solver.findWords(words) == expected