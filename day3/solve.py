from advent_of_code_2024.utils.input_handling import (
    read_file,
    parse_args,
)
from advent_of_code_2024.day3.solver import (
    solve,
)

def main():
    args = parse_args()
    input = open(args.input_file,'r').read()
    if args.part == 1:
        use_do_dont_rule=False
    if args.part == 2:
        use_do_dont_rule=True
    output = solve(input, use_do_dont_rule)
    print(f"Output: {output}")
    return output


if __name__ == "__main__":
    main()
    