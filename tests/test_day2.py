import pytest
from advent_of_code_2024.day2.solver import (
    solve_part_1,
    solve_part_2,
)
from advent_of_code_2024.utils import input_handling

TEST_INPUT_FILE = "./tests/test_inputs/day2.txt"


@pytest.mark.parametrize("expected", [2])
def test_solver_part1(expected):
    input = input_handling.read_regular_input(TEST_INPUT_FILE, dtype=int)
    result = solve_part_1(input)
    print(result)
    assert result == expected


@pytest.mark.parametrize("expected", [4])
def test_solver_part2(expected):
    input = input_handling.read_regular_input(TEST_INPUT_FILE, dtype=int)
    result = solve_part_2(input)
    assert result == expected
