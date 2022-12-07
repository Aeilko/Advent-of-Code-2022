from collections import deque
from pprint import pprint

from utils.aoc import check_for_input_file
from utils.file import read_file_content


def parse_tree(lines: list) -> dict:
    root = {}
    cur = root
    parents = deque()
    i = 0
    while i < len(lines):
        line = lines[i].split()
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "/":
                    cur = root
                    parents = deque()
                elif line[2] == "..":
                    cur = parents.pop()
                else:
                    parents.append(cur)
                    cur = cur[line[2]]
            elif line[1] == "ls":
                while i+1 < len(lines) and lines[i+1][0] != "$":
                    i += 1
                    l = lines[i].split()
                    if l[0] == "dir":
                        cur[l[1]] = {}
                    else:
                        size = int(l[0])
                        cur[l[1]] = size
        i += 1
    return root


def get_all_sizes(root: dict) -> (int, list):
    r = []
    s = 0
    for x in root:
        if type(root[x]) is int:
            s += root[x]
        else:
            f, l = get_all_sizes(root[x])
            s += f
            r.append(f)
            r.extend(l)
    return s, r


def solve_part1(input: str) -> int:
    lines = input[:-1].split("\n")
    root = parse_tree(lines)
    total, sizes = get_all_sizes(root)
    r = 0
    for d in sizes:
        if d <= 100000:
            r += d

    return r


def solve_part2(input: str) -> int:
    lines = input[:-1].split("\n")
    root = parse_tree(lines)
    total, sizes = get_all_sizes(root)

    diff = total - 40000000

    r = 70000000
    for x in sizes:
        if diff <= x < r:
            r = x

    return r


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
