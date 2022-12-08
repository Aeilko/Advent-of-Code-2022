from utils.aoc import check_for_input_file
from utils.file import read_file_content


def solve_part1(input: str) -> int:
    lines = input[:-1].split("\n")
    r = 0
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            tree = int(lines[y][x])

            top =   [int(lines[i][x]) for i in range(y - 1, -1, -1)]
            right = [int(lines[y][i]) for i in range(x + 1, len(lines[y]))]
            bottom =[int(lines[i][x]) for i in range(y + 1, len(lines))]
            left =  [int(lines[y][i]) for i in range(x - 1, -1, -1)]

            v = False
            for row in [top, left, bottom, right]:
                vis = True
                for val in row:
                    if val >= tree:
                        vis = False
                        break
                if vis:
                    v = True
                    break

            if v:
                r += 1

    return r


def solve_part2(input: str) -> int:
    lines = input[:-1].split("\n")
    r = -1
    # Skip the edges, since they have a 0 on one side, so the scenic score is always 0
    for y in range(1, len(lines)-1):
        for x in range(1, len(lines[y])-1):
            tree = int(lines[y][x])

            top =   [int(lines[i][x]) for i in range(y-1, -1, -1)]
            right = [int(lines[y][i]) for i in range(x+1, len(lines[y]))]
            bottom =[int(lines[i][x]) for i in range(y+1, len(lines))]
            left =  [int(lines[y][i]) for i in range(x-1, -1, -1)]
            score = 1
            for row in [top, right, bottom, left]:
                trees = 0
                for val in row:
                    trees += 1
                    if val >= tree:
                        break
                score *= trees

            if score > r:
                r = score

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
