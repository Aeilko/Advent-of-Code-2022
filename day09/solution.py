from utils.aoc import check_for_input_file
from utils.file import read_file_content


def solve_part1(input: str) -> int:
    lines = input[:-1].split("\n")

    head = (0, 0)
    tail = (0, 0)
    visited = set()

    moves = {'U': (0, 1), 'R': (1, 0), 'D': (0, -1), 'L': (-1, 0)}
    for line in lines:
        (direction, steps) = line.split()
        for _ in range(int(steps)):
            head = (head[0]+moves[direction][0], head[1]+moves[direction][1])
            tdx = head[0]-tail[0]
            tdy = head[1]-tail[1]
            tm = (0, 0)
            if abs(tdx) > 1 or abs(tdy) > 1:
                tm = (int(tdx/abs(tdx)) if tdx != 0 else 0, int(tdy/abs(tdy)) if tdy != 0 else 0)
            tail = (tail[0]+tm[0], tail[1]+tm[1])
            visited.add(tail)

    return len(visited)


def solve_part2(input: str) -> int:
    lines = input[:-1].split("\n")

    knots = []
    for _ in range(10):
        knots.append((0, 0))
    visited = set()

    moves = {'U': (0, 1), 'R': (1, 0), 'D': (0, -1), 'L': (-1, 0)}
    for line in lines:
        (direction, steps) = line.split()
        for _ in range(int(steps)):
            knots[0] = (knots[0][0] + moves[direction][0], knots[0][1] + moves[direction][1])
            for i in range(1, 10):
                tdx = knots[i-1][0] - knots[i][0]
                tdy = knots[i-1][1] - knots[i][1]
                tm = (0, 0)
                if abs(tdx) > 1 or abs(tdy) > 1:
                    tm = (int(tdx / abs(tdx)) if tdx != 0 else 0, int(tdy / abs(tdy)) if tdy != 0 else 0)
                knots[i] = (knots[i][0] + tm[0], knots[i][1] + tm[1])
            visited.add(knots[9])

    return len(visited)


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
