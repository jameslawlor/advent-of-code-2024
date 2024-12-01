def compute_distance(i, j):
    return abs(i - j)


def solve_part_1(input):
    (list1, list2) = input
    list1_ordered = list(sorted(list1))
    list2_ordered = list(sorted(list2))

    total_distance = 0

    for i, j in zip(list1_ordered, list2_ordered):
        total_distance += compute_distance(i, j)

    return total_distance


def compute_similarity(i, lst):
    return i * lst.count(i)


def solve_part_2(input):
    (list1, list2) = input

    total_similarity_score = 0

    for element in list1:
        total_similarity_score += compute_similarity(element, list2)

    return total_similarity_score
