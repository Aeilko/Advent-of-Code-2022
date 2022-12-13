import json
from functools import cmp_to_key

from utils.aoc import check_for_input_file
from utils.file import read_file_content

def compare(l1, l2):
    r = 0
    for i in range(len(l1)):
        if len(l2) <= i:
            r = 1
        elif type(l1[i]) == int and type(l2[i]) == int:
            if l1[i] < l2[i]:
                r = -1
            elif l1[i] > l2[i]:
                r = 1
        elif type(l1[i]) == list and type(l2[i]) == list:
            r = compare(l1[i], l2[i])
        else:
            if type(l1[i]) == int:
                r = compare([l1[i]], l2[i])
            else:
                r = compare(l1[i], [l2[i]])

        if r != 0:
            break

    if r == 0 and len(l1) < len(l2):
        r = -1

    return r


def solve_part1(input: str) -> int:
    pairs = input[:-1].split("\n\n")
    r = 0
    for i in range(len(pairs)):
        (left, right) = map(json.loads, pairs[i].split("\n"))
        if compare(left, right) == -1:
            r += (i+1)

    return r


def solve_part2(input: str) -> int:
    pairs = input[:-1].split("\n\n")
    list = [[[2]], [[6]]]
    for i in range(len(pairs)):
        (left, right) = map(json.loads, pairs[i].split("\n"))
        list.append(left)
        list.append([right])

    sorted_list = sorted(list, key=cmp_to_key(compare))

    return (sorted_list.index([[2]]) + 1) * (sorted_list.index([[6]]) + 1)


def test_part1():
    input = read_file_content("inputs/test")
    answer = int(read_file_content("inputs/ans1"))

    result = solve_part1(input)
    if result == answer:
        print("Test successful")
    else:
        print("Test unsuccessful: " + str(result) + ", expected: " + str(answer))


def test_part2():
    input = read_file_content("inputs/test")
    answer = int(read_file_content("inputs/ans2"))

    result = solve_part2(input)
    if result == answer:
        print("Test successful")
    else:
        print("Test unsuccessful: " + str(result) + ", expected: " + str(answer))


if __name__ == '__main__':
    # Check if we have an input file, if not, download it
    check_for_input_file()

    # Perform this day's solution
    input = read_file_content("inputs/input")

    print(" --- Part 1 --- ")
    test_part1()
    print("Part 1 result:\t" + str(solve_part1(input)))

    print("\n --- Part 2 ---")
    test_part2()
    print("Part 2 result:\t" + str(solve_part2(input)))
