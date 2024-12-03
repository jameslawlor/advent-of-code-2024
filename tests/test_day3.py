import pytest
from advent_of_code_2024.day3.solver import (
    instruction_compute,
)

@pytest.mark.parametrize("input, expected", [
   ["xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))", 161],
   ["xmul(2,4)", 8],
   ["%&mul[3,7]!@^do_not_mul(5,5)", 25],
   ["mul(11,8)mul(8,5)", 128],
])
def test_instruction_compute(input, expected):
    result = instruction_compute(input)
    print(result)
    assert result == expected


