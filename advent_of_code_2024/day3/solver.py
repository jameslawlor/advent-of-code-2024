import re
import math


def find_valid_substrings(s, match_str=r'mul\(\d+,\d+\)'):
    return re.findall(match_str, s)


def instruction_compute(instruction):

    score = 0

    valid_muls = find_valid_substrings(instruction)
    
    for m in valid_muls:
        found_ints = find_valid_substrings(m, match_str=r'\d+')
        score += math.prod(map(int, found_ints))

    return score

def solve_part_1(input, ):

    total = 0
    for instruction in input:
        score = instruction_compute(instruction)
        total+=score

    return total


def solve_part_2(input,):

    return