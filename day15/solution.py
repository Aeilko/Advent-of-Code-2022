from utils.aoc import check_for_input_file
from utils.file import read_file_content
from utils.grid import display_dict_grid


def parse_input(lines, target):
    grid = {}
    for line in lines:
        (sensor, beacon) = line[12:].split(": closest beacon is at x=")
        sx, sy = [int(i) for i in sensor.split(", y=")]
        bx, by = [int(i) for i in beacon.split(", y=")]
        grid[(sx, sy)] = "S"
        grid[(bx, by)] = "B"
        distance = abs(sx-bx) + abs(sy-by)
        dxmax = distance - abs(target-sy)
        if dxmax > 0:
            for dx in range(dxmax+1):
                for ddx in [dx, dx*-1]:
                    nx = sx+ddx
                    if (nx, target) not in grid:
                        grid[(nx, target)] = "#"

    return grid


def solve_part1(input: str, target=2000000) -> int:
    lines = input[:-1].split("\n")

    grid = parse_input(lines, target)

    r = 0
    for (x, y) in grid:
        if y == target:
            if grid[(x, y)] == "#":
                r += 1
    return r


def solve_part2(input: str, max=4000000) -> int:
    lines = input[:-1].split("\n")
    sensors = []
    edges = set()
    for line in lines:
        (sensor, beacon) = line[12:].split(": closest beacon is at x=")
        sx, sy = [int(i) for i in sensor.split(", y=")]
        bx, by = [int(i) for i in beacon.split(", y=")]
        d = abs(sx-bx) + abs(sy-by)
        sensors.append(((sx, sy), d))

        # Add all coords that are next to the border
        for i in range(d + 2):
            j = (d - i) + 1
            for (dx, dy) in [(i, j), (i * -1, j), (i, j * -1), (i * -1, j * -1)]:
                nx = sx + dx
                ny = sy + dy
                if 0 <= nx <= max and 0 <= ny <= max:
                    edges.add((nx, ny))

    print("Coords to check", len(edges))

    r = -1
    for (x, y) in edges:
        valid = True
        for ((sx, sy), d) in sensors:
            if abs(x - sx) + abs(y - sy) <= d:
                valid = False
                break
        if valid:
            r = x * 4000000 + y
            break

    return r


def test_part1():
    input = read_file_content("inputs/test")
    answer = int(read_file_content("inputs/ans1"))

    result = solve_part1(input, 10)
    if result == answer:
        print("Test successful")
    else:
        print("Test unsuccessful: " + str(result) + ", expected: " + str(answer))


def test_part2():
    input = read_file_content("inputs/test")
    answer = int(read_file_content("inputs/ans2"))

    result = solve_part2(input, 20)
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
