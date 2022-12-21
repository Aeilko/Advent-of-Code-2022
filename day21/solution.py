from utils.aoc import check_for_input_file
from utils.file import read_file_content


OPS = {
    '+': lambda l, r: l + r,
    '-': lambda l, r: l - r,
    '*': lambda l, r: l * r,
    '/': lambda l, r: l/r,
}

def get_value(name, monkeys):
    if type(monkeys[name]) is int:
        return monkeys[name]
    else:
        (l, token, r) = monkeys[name].split(" ")
        return int(OPS[token](get_value(l, monkeys), get_value(r, monkeys)))


def solve_part1(input: str) -> int:
    lines = input[:-1].split("\n")

    monkeys = {}
    for line in lines:
        (name, proc) = line.split(": ")
        monkeys[name] = int(proc) if proc.isnumeric() else proc

    return get_value("root", monkeys)


UP = "NEXT_VAL"
def solve_part2(input: str) -> int:
    lines = input[:-1].split("\n")

    monkeys = {}
    for line in lines:
        (name, proc) = line.split(": ")
        monkeys[name] = int(proc) if proc.isnumeric() else proc

    func = UP
    cur_name = "humn"
    while cur_name != "root":
        for name in monkeys:
            if type(monkeys[name]) != int:
                (l, token, r) = monkeys[name].split(" ")
                if cur_name in [l, r]:
                    if name == "root":
                        if cur_name == l:
                            func = func.replace(UP, str(get_value(r, monkeys)))
                        elif  cur_name == r:
                            func = func.replace(UP, str(get_value(l, monkeys)))
                        cur_name = "root"
                        break
                    else:
                        cur_func = ""
                        if cur_name == l:
                            r_val = str(get_value(r, monkeys))
                            if token == '-':
                                cur_func = UP + "+" + r_val
                            elif token == '+':
                                cur_func = UP + "-" + r_val
                            elif token == '*':
                                cur_func = UP + "/" + r_val
                            elif token == '/':
                                cur_func = UP + "*" + r_val
                        elif cur_name == r:
                            l_val = str(get_value(l, monkeys))
                            if token == '-':
                                cur_func = l_val + "-" + UP
                            elif token == '+':
                                cur_func = UP + "-" + l_val
                            elif token == '*':
                                cur_func = UP + "/" + l_val
                            elif token == '/':
                                cur_func = l_val + "/" + UP
                        func = func.replace(UP, "(" + cur_func + ")")
                        cur_name = name
                        break
    return int(eval(func))


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
