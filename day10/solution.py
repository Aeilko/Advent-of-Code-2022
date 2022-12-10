from utils.aoc import check_for_input_file
from utils.file import read_file_content


def solve_part1(input: str) -> int:
    lines = input[:-1].split("\n")

    cycle = 1
    x = 1
    r = 0
    for line in lines:
        args = line.split()
        if args[0] == "noop":
            if (cycle+20) % 40 == 0:
                r += cycle*x
            cycle += 1
        elif args[0] == "addx":
            if (cycle+20) % 40 == 0:
                r += cycle*x
            cycle += 1
            if (cycle+20) % 40 == 0:
                r += cycle*x
            cycle += 1
            x += int(args[1])
        else:
            print("Unknown command", args[1])

    return r


def increase_cycle(cycle, x, out):
    dx = (cycle % 40) - x
    out += '#' if abs(dx) < 2 else '.'
    cycle += 1
    return cycle, out


def solve_part2(input: str) -> int:
    lines = input[:-1].split("\n")

    cycle = 0
    x = 1
    r = ""
    for line in lines:
        args = line.split()
        if args[0] == "noop":
            (cycle, r) = increase_cycle(cycle, x, r)
        elif args[0] == "addx":
            (cycle, r) = increase_cycle(cycle, x, r)
            (cycle, r) = increase_cycle(cycle, x, r)
            x += int(args[1])
        else:
            print("Unknown command", args[1])

    line = ""
    for i in range(len(r)):
        if i % 40 == 0:
            print(line)
            line = ""
        line += r[i]
    print(line)

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
    answer = read_file_content("inputs/ans2")

    result = solve_part2(input)
    if result != answer:
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
    solve_part2(input)
