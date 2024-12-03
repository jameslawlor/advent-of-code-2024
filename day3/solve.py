from advent_of_code_2024.utils.input_handling import (
    read_file,
    parse_args,
)
from advent_of_code_2024.day3.solver import (
    solve_part_1,
    solve_part_2,
)

def main():
    args = parse_args()
    input = read_file(args.input_file)
    if args.part == 1:
        output = solve_part_1(input)
    if args.part == 2:
        output = solve_part_2(input)
    print(f"Output: {output}")
    return output


if __name__ == "__main__":
    main()
    