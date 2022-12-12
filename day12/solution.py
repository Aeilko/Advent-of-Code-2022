import string
from queue import PriorityQueue

from utils.aoc import check_for_input_file
from utils.file import read_file_content


def shortest_path(start, end, grid):
    to_visit = PriorityQueue()
    to_visit.put((0, start))
    visited = set()
    r = -1
    while not to_visit.empty() and r == -1:
        (cost, (x, y)) = to_visit.get()
        if (x, y) in visited:
            continue
        for (dx, dy) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < len(grid[y]) and 0 <= ny < len(grid):
                if grid[ny][nx] - grid[y][x] < 2:
                    if (nx, ny) == end:
                        r = cost + 1
                        break
                    if (nx, ny) not in visited:
                        to_visit.put((cost + 1, (nx, ny)))
        visited.add((x, y))

    return r


def solve_part1(input: str) -> int:
    lines = input[:-1].split("\n")

    heights = "S" + string.ascii_lowercase + "E"
    start = (0, 0)
    end = (0, 0)
    grid = [[]] * len(lines)
    for y in range(len(lines)):
        grid[y] = [0] * len(lines[y])
        for x in range(len(lines[y])):
            grid[y][x] = heights.index(lines[y][x])
            if lines[y][x] == 'S':
                start = (x, y)
            elif lines[y][x] == 'E':
                end = (x, y)

    return shortest_path(start, end, grid)


def solve_part2(input: str) -> int:
    lines = input[:-1].split("\n")

    heights = "S" + string.ascii_lowercase + "E"
    end = (0, 0)
    grid = [[]] * len(lines)
    for y in range(len(lines)):
        grid[y] = [0] * len(lines[y])
        for x in range(len(lines[y])):
            grid[y][x] = heights.index(lines[y][x])
            if lines[y][x] == 'E':
                end = (x, y)

    r = len(grid)*len(grid[0])
    for sx in range(len(grid[0])):
        for sy in range(len(grid)):
            if grid[sy][sx] == 1:
                rr = shortest_path((sx, sy), end, grid)
                if rr != -1 and rr < r:
                    r = rr
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
