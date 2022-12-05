from collections import deque

from utils.aoc import check_for_input_file
from utils.file import read_file_content


def solve_part1(input: str) -> int:
    (state, moves) = input[:-1].split("\n\n")
    state = state.split("\n")
    moves = moves.split("\n")
    num_stacks = int(state[-1][-2])
    stacks = []

    for i in range(num_stacks):
        q = deque()
        index = 1 + (4*i)
        for j in range(len(state)-2, -1, -1):
            if len(state[j]) >= index and state[j][index] != ' ':
                q.append(state[j][index])
        stacks.append(q)

    for move in moves:
        m = move.split(" ")
        x = int(m[1])
        f = int(m[3])
        t = int(m[5])
        for _ in range(x):
            stacks[t-1].append(stacks[f-1].pop())

    r = ""
    for s in stacks:
        r = r + s.pop()
    print(r)

    return -1


def solve_part2(input: str) -> int:
    (state, moves) = input[:-1].split("\n\n")
    state = state.split("\n")
    moves = moves.split("\n")
    num_stacks = int(state[-1][-2])
    stacks = []

    for i in range(num_stacks):
        q = deque()
        index = 1 + (4 * i)
        for j in range(len(state) - 2, -1, -1):
            if len(state[j]) >= index and state[j][index] != ' ':
                q.append(state[j][index])
        stacks.append(q)

    for move in moves:
        m = move.split(" ")
        x = int(m[1])
        f = int(m[3])
        t = int(m[5])
        items = []
        for _ in range(x):
            items.append(stacks[f - 1].pop())
        for i in range(x-1, -1, -1):
            stacks[t-1].append(items[i])

    r = ""
    for s in stacks:
        r = r + s.pop()
    print(r)

    return -1


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
