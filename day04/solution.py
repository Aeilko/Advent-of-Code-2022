from utils.aoc import check_for_input_file
from utils.file import read_file_content


def solve_part1(input: str) -> int:
    lines = input[:-1].split("\n")
    r = 0
    for line in lines:
        first, second = line.split(",")
        fs, fe = map(int, first.split("-"))
        ss, se = map(int, second.split("-"))
        if (fs <= ss and fe >= se) or (ss <= fs and se >= fe):
            r += 1

    return r


def solve_part2(input: str) -> int:
    lines = input[:-1].split("\n")
    r = 0
    for line in lines:
        first, second = line.split(",")
        fs, fe = map(int, first.split("-"))
        ss, se = map(int, second.split("-"))
        if (fs <= ss <= fe) or (fs <= se <= fe) or (ss <= fs <= se) or (ss <= fe <= se):
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
