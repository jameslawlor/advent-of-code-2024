import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_file",
    )
    parser.add_argument("--part", type=int)
    args = parser.parse_args()
    return args


def read_regular_input(f, dtype=str):
    with open(f, "r") as input_file:
        data = [list(map(dtype, line.rstrip("\n").split())) for line in input_file]
    return data


def read_side_by_side_list_format(f, dtype=str):
    
    data = read_regular_input(f, dtype)

    list1 = []
    list2 = []

    for line in data:
        list1.append(int(line[0]))
        list2.append(int(line[1]))

    return (list1, list2)
