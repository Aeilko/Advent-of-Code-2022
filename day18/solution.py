import sys

from utils.aoc import check_for_input_file
from utils.file import read_file_content


def parse_input(lines):
    grid = set()
    for line in lines:
        (x, y, z) = [int(x) for x in line.split(',')]
        grid.add((x, y, z))
    return grid


def solve_part1(input: str) -> int:
    lines = input[:-1].split("\n")

    grid = parse_input(lines)
    r = 0
    for (x, y, z) in grid:
        for (dx, dy, dz) in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            if (x+dx, y+dy, z+dz) not in grid:
                r += 1
    return r


def solve_part2(input: str) -> int:
    lines = input[:-1].split("\n")

    grid = parse_input(lines)
    r = 0
    xs = [x for (x, _, _) in grid]
    ys = [y for (_, y, _) in grid]
    zs = [z for (_, _, z) in grid]
    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)
    min_z = min(zs)
    max_z = max(zs)
    # Create a set of all possible coordinates, with a border of width 1 around the obsidian.
    empty_spaces = set()
    for x in range(min_x-1, max_x+2):
        for y in range(min_y-1, max_y+2):
            for z in range(min_z-1, max_z+2):
                empty_spaces.add((x, y, z))

    # Remove the obsidian spaces from the set of empty spaces and count the visible sides
    for (x, y, z) in grid:
        empty_spaces.remove((x, y, z))
        for (dx, dy, dz) in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            if (x + dx, y + dy, z + dz) not in grid:
                r += 1

    # Check which empty spaces are reachable from the outside of the obsidian and remove them from the empty set
    to_visit = set()
    to_visit.add((min_x-1, min_y-1, min_z-1))
    while len(to_visit) > 0:
        (x, y, z) = to_visit.pop()
        empty_spaces.remove((x, y, z))
        for (dx, dy, dz) in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            n_coord = (x+dx, y+dy, z+dz)
            if n_coord in empty_spaces and n_coord not in to_visit:
                to_visit.add(n_coord)

    # Everything left in the empty spaces set is unreachable from the outside, and therefore inside.
    # Remove the sides bordering these spaces
    for (x, y, z) in empty_spaces:
        for (dx, dy, dz) in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            if (x+dx, y+dy, z+dz) in grid:
                r -= 1
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
