import pytest
from advent_of_code_2024.utils import input_handling

TEST_INPUT_FILE = "./tests/test_inputs/day1.txt"


@pytest.mark.parametrize(
    "expected",
    [
        (
            [
                3,
                4,
                2,
                1,
                3,
                3,
            ],
            [
                4,
                3,
                5,
                3,
                9,
                3,
            ],
        )
    ],
)
def test_read_side_by_side_list_format(expected):
    result = input_handling.read_side_by_side_list_format(TEST_INPUT_FILE)
    assert result == expected
