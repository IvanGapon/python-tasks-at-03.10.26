import pytest

from task_128_longest_consecutive_sequence.solution_128 import Solution


@pytest.fixture
def solver():
    return Solution()


@pytest.mark.parametrize(
    "nums, expected",
    [
        # --- Базовые примеры из задачи ---
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([1, 0, 1, 2], 3),

        # --- Граничные случаи (пустой список и 1 элемент) ---
        ([], 0),
        ([5], 1),
        ([0], 1),

        # --- Дубликаты ---
        ([1, 1, 1, 1], 1),
        ([2, 2, 3, 3, 4, 4], 3),

        # --- Отрицательные числа ---
        ([-5, -4, -3, -2, -1], 5),
        ([-1, -2, -3, 0, 1], 5),
        ([-10, -9, 0, 1, 2, 100], 3),

        # --- Несколько последовательностей разной длины ---
        ([10, 11, 12, 1, 2, 3, 4, 20, 21], 4),
        ([100, 4, 200, 1, 3, 2, 101, 102, 103, 104], 5),

        # --- Большие числа / Стресс-тесты ---
        (list(range(10000)), 10000),
        (list(range(10000, 0, -1)), 10000),
    ],
)
def test_longest_consecutive(solver, nums: list[int], expected: int):
    assert solver.longestConsecutive(nums) == expected