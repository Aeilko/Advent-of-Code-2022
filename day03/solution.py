from utils.file import read_file_content


def solve_part1(input: str) -> int:
    lines = input.split("\n")
    r = 0
    for line in lines:
        half = int(len(line)/2)
        a = line[:half]
        b = line[half:]
        found = False
        for c in a:
            if c in b:
                n = ord(c)
                if n > 96:
                    r += n-96
                else:
                    r += n-38
                found = True
                break
        if found:
            continue

    return r


def solve_part2(input: str) -> int:
    lines = input.split("\n")
    r = 0
    groups = int(len(lines)/3)
    for i in range(groups):
        a = lines[i*3]
        b = lines[i*3 + 1]
        c = lines[i*3 + 2]
        found = False
        for x in a:
            if x in b and x in c:
                n = ord(x)
                if n > 96:
                    r += n - 96
                else:
                    r += n - 38
                found = True
                break

        if found:
            continue

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

    input = read_file_content("inputs/input")

    print(" --- Part 1 --- ")
    test_part1()
    print("Part 1 result:\t" + str(solve_part1(input)))

    print("\n --- Part 2 ---")
    test_part2()
    print("Part 2 result:\t" + str(solve_part2(input)))
