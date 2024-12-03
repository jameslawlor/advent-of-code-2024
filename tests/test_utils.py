import pytest
from advent_of_code_2024.utils import input_handling


@pytest.mark.parametrize(
    "test_input_file, expected",
    [
        (
            "./tests/test_inputs/day1.txt", 
            (
                [3, 4, 2, 1, 3, 3],
                [4, 3, 5, 3, 9, 3],
            )
        ),
    ],
)
def test_read_side_by_side_list_format(test_input_file, expected):
    result = input_handling.read_side_by_side_list_format(test_input_file, dtype=int)
    assert result == expected



@pytest.mark.parametrize(
    "test_input_file, expected",
    [
        (
            "./tests/test_inputs/day2.txt",
            [
                [7, 6, 4, 2, 1,],
                [1, 2, 7, 8, 9,],
                [9, 7, 6, 2, 1,],
                [1, 3, 2, 4, 5,],
                [8, 6, 4, 4, 1,],
                [1, 3, 6, 7, 9,],
            ]
        )
    ],
)
def test_read_regular_input(test_input_file, expected):
    result = input_handling.read_regular_input(test_input_file, dtype=int)
    assert result == expected
