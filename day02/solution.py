from utils.aoc import check_for_input_file
from utils.file import read_file_content


def solve_part1(input: str) -> int:
    lines = input[:-1].split("\n")

    r = 0
    for line in lines:
        (elf, me) = line.split(" ")
        if me == 'X':
            r += 1
            if elf == 'A':
                r += 3
            elif elf == 'C':
                r += 6
        elif me == 'Y':
            r += 2
            if elf == 'A':
                r += 6
            elif elf == 'B':
                r += 3
        elif me == 'Z':
            r += 3
            if elf == 'B':
                r += 6
            elif elf == 'C':
                r += 3

    return r


def solve_part2(input: str) -> int:
    lines = input[:-1].split("\n")

    r = 0
    for line in lines:
        (elf, result) = line.split(" ")
        me = ''
        if result == 'X':
            if elf == 'A':
                me = 'Z'
            elif elf == 'B':
                me = 'X'
            elif elf == 'C':
                me = 'Y'
        elif result == 'Y':
            if elf == 'A':
                me = 'X'
            elif elf == 'B':
                me = 'Y'
            elif elf == 'C':
                me = 'Z'
        elif result == 'Z':
            if elf == 'A':
                me = 'Y'
            elif elf == 'B':
                me = 'Z'
            elif elf == 'C':
                me = 'X'

        if me == 'X':
            r += 1
            if elf == 'A':
                r += 3
            elif elf == 'C':
                r += 6
        elif me == 'Y':
            r += 2
            if elf == 'A':
                r += 6
            elif elf == 'B':
                r += 3
        elif me == 'Z':
            r += 3
            if elf == 'B':
                r += 6
            elif elf == 'C':
                r += 3

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
