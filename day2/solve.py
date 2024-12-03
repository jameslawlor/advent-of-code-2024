from advent_of_code_2024.utils.input_handling import (
    read_regular_input,
    parse_args,
)
from advent_of_code_2024.day2.solver import (
    solve_part_1,
    solve_part_2,
)

def main():
    args = parse_args()
    input = read_regular_input(args.input_file, dtype=int)
    if args.part == 1:
        output = solve_part_1(input)
    if args.part == 2:
        output = solve_part_2(input)
    print(f"Output: {output}")
    return output


if __name__ == "__main__":
    main()
    