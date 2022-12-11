import math
from collections import deque

from utils.aoc import check_for_input_file
from utils.file import read_file_content


def solve_part1(input: str) -> int:
    inp_monkies = input[:-1].split("\n\n")
    monkies = []
    MOD = 3
    for inp_monk in inp_monkies:
        inp = inp_monk.split("\n")
        items = deque(reversed([int(x) for x in inp[1].split(": ")[1].split(", ")]))
        operation = inp[2].split(" = ")[1]
        divisor = int(inp[3].split(" ")[-1])
        MOD *= divisor
        div_true = int(inp[4].split(" ")[-1])
        div_false = int(inp[5].split(" ")[-1])
        m = {
            'items': items,
            'operation': operation,
            'divisor': divisor,
            'div_true': div_true,
            'div_false': div_false,
            'count': 0
        }
        monkies.append(m)

    for _ in range(20):
        for m in monkies:
            while len(m['items']) > 0:
                old = m['items'].pop()
                new = eval(m['operation']) % MOD
                new = math.floor(new/3)
                if new % m['divisor'] == 0:
                    monkies[m['div_true']]['items'].appendleft(new)
                else:
                    monkies[m['div_false']]['items'].appendleft(new)
                m['count'] += 1

    counts = sorted([m['count'] for m in monkies], reverse=True)
    return counts[0]*counts[1]


def solve_part2(input: str) -> int:
    inp_monkies = input[:-1].split("\n\n")
    monkies = []
    MOD = 1
    for inp_monk in inp_monkies:
        inp = inp_monk.split("\n")
        items = deque(reversed([int(x) for x in inp[1].split(": ")[1].split(", ")]))
        operation = inp[2].split(" = ")[1]
        divisor = int(inp[3].split(" ")[-1])
        MOD *= divisor
        div_true = int(inp[4].split(" ")[-1])
        div_false = int(inp[5].split(" ")[-1])
        m = {
            'items': items,
            'operation': operation,
            'divisor': divisor,
            'div_true': div_true,
            'div_false': div_false,
            'count': 0
        }
        monkies.append(m)

    for _ in range(10000):
        for m in monkies:
            while len(m['items']) > 0:
                old = m['items'].pop()
                new = eval(m['operation']) % MOD
                if new % m['divisor'] == 0:
                    monkies[m['div_true']]['items'].appendleft(new)
                else:
                    monkies[m['div_false']]['items'].appendleft(new)
                m['count'] += 1

    counts = sorted([m['count'] for m in monkies], reverse=True)
    return counts[0] * counts[1]


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
