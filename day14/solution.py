from utils.aoc import check_for_input_file
from utils.file import read_file_content
from utils.grid import display_dict_grid


def parse_grid(lines):
    maxy = 0
    grid = {}
    for line in lines:
        steps = line.split(" -> ")
        prev_step = (-1, -1)
        for step in steps:
            (px, py) = prev_step
            x, y = [int(i) for i in step.split(",")]
            (dx, dy) = (x - px, y - py)
            maxy = y if y > maxy else maxy
            if prev_step == (-1, -1):
                grid[(x, y)] = "#"
                prev_step = (x, y)
                continue
            if dx != 0:
                for ddx in range(1, abs(dx) + 1):
                    if dx < 0:
                        grid[(px - ddx, py)] = "#"
                    else:
                        grid[(px + ddx, py)] = "#"
            if dy != 0:
                for ddy in range(1, abs(dy) + 1):
                    if dy < 0:
                        grid[(px, py - ddy)] = "#"
                    else:
                        grid[(px, py + ddy)] = "#"
            prev_step = (x, y)
    return grid, maxy


def solve_part1(input: str) -> int:
    lines = input[:-1].split("\n")
    spawn = (500, 0)

    grid, maxy = parse_grid(lines)

    r = 0
    abyss = False
    while not abyss:
        (x, y) = spawn
        while True:
            dropped = False
            for (dx, dy) in [(0, 1), (-1, 1), (1, 1)]:
                if (x+dx, y+dy) not in grid:
                    x += dx
                    y += dy
                    dropped = True
                    break

            if not dropped:
                grid[(x, y)] = "o"
                break

            if y > maxy:
                abyss = True
                break
        r += 1

    # We found the first sand that fell into the abyss, we need the amount that didnt fall into the abyss
    return r-1


def solve_part2(input: str) -> int:
    lines = input[:-1].split("\n")
    spawn = (500, 0)

    grid, maxy = parse_grid(lines)

    r = 0
    while spawn not in grid:
        (x, y) = spawn
        while True:
            dropped = False
            for (dx, dy) in [(0, 1), (-1, 1), (1, 1)]:
                if (x + dx, y + dy) not in grid:
                    x += dx
                    y += dy
                    dropped = True
                    break

            if not dropped:
                grid[(x, y)] = "o"
                break

            if y > maxy:
                grid[(x, y)] = "o"
                break
        r += 1
    
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
