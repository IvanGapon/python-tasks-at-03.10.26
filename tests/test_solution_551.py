import pytest
from task_551_student_attendance_record.solution_551 import Solution


@pytest.fixture
def solver():
    return Solution()


@pytest.mark.parametrize(
    "s, expected",
    [
        # --- Базовые примеры из задачи ---
        ("PPALLP", True),
        ("PPALLL", False),

        # --- Граничные случаи по 'A' (Отсутствие) ---
        ("P", True),
        ("A", True),
        ("AA", False),
        ("PAALLP", False),

        # --- Граничные случаи по 'L' (Опоздания) ---
        ("LL", True),
        ("LLL", False),
        ("LLLL", False),
        ("LPLPLPL", True),
        ("LLPLLP", True),
        ("LLPALLL", False),

        # --- Комбинации параметров ---
        ("PALP", True),
        ("LALL", True),
        ("ALL", True),
        ("LLA", True),

        # --- Длинные строки / Стресс-тесты ---
        ("P" * 10000, True),
        ("P" * 5000 + "A" + "P" * 5000, True),
        ("P" * 5000 + "AA" + "P" * 5000, False),
        ("P" * 5000 + "LLL" + "P" * 5000, False),
    ],
)
def test_check_record(solver, s: str, expected: bool):
    assert solver.checkRecord(s) == expected