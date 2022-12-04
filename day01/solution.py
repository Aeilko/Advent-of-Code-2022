from utils.file import read_file_content


def solve_part1(input: str) -> int:
    lines = input[:-1].split("\n\n")
    r = -1

    for elf in lines:
        l = elf.split("\n")
        s = 0
        for x in l:
            s += int(x)
        if s > r:
            r = s

    return r


def solve_part2(input: str) -> int:
    lines = input[:-1].split("\n\n")

    sums = []
    for elf in lines:
        l = elf.split("\n")
        s = 0
        for x in l:
            s += int(x)

        sums.append(s)

    sums.sort(reverse=True)
    return sum(sums[0:3])


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
