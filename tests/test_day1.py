import pytest
from advent_of_code_2024.day1.solver import (
    solve_part_1,
    solve_part_2,
)
from advent_of_code_2024.utils import input_handling

TEST_INPUT_FILE = "./tests/test_inputs/day1.txt"


@pytest.mark.parametrize("expected", [11])
def test_solver_part1(expected):
    input = input_handling.read_side_by_side_list_format(TEST_INPUT_FILE)
    result = solve_part_1(input)
    assert result == expected


@pytest.mark.parametrize("expected", [31])
def test_solver_part2(expected):
    input = input_handling.read_side_by_side_list_format(TEST_INPUT_FILE)
    result = solve_part_2(input)
    assert result == expected
