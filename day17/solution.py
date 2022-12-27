from utils.aoc import check_for_input_file
from utils.file import read_file_content


SHAPES = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (0, 1), (1, 1)]
]


def add_rock(board, moves, highest_y, rock_counter, move_counter):
    # Spawn rock
    cur_rock = {}
    (x, y) = (2, highest_y + 4)
    shape = SHAPES[(rock_counter % len(SHAPES))]
    min_x = 2
    max_x = 0
    max_y = 0
    for (dx, dy) in shape:
        cur_rock[(x + dx, y + dy)] = True
        max_x = max(x + dx, max_x)
        max_y = max(y + dy, max_y)

    # Moving loop
    while True:
        # Move sideways
        move = moves[(move_counter % len(moves))]
        if move == '<' and min_x > 0:
            new_rock = {}
            for (x, y) in cur_rock:
                new_rock[(x - 1, y)] = True

            can_move = True
            for (x, y) in new_rock:
                if (x, y) in board:
                    can_move = False
                    break
            if can_move:
                min_x -= 1
                max_x -= 1
                cur_rock = new_rock
        elif move == '>' and max_x < 6:
            new_rock = {}
            for (x, y) in cur_rock:
                new_rock[(x + 1, y)] = True
            can_move = True
            for (x, y) in new_rock:
                if (x, y) in board:
                    can_move = False
                    break
            if can_move:
                min_x += 1
                max_x += 1
                cur_rock = new_rock
        move_counter += 1

        # Move down
        can_move = True
        for (x, y) in cur_rock:
            if (x, y - 1) in board:
                can_move = False
                break
            elif y - 1 < 0:
                can_move = False
                break
        if can_move:
            # Can move down
            new_rock = {}
            for (x, y) in cur_rock:
                new_rock[(x, y - 1)] = True
            max_y -= 1
            cur_rock = new_rock
        else:
            # Cant move, save rock and continue to the next rock
            for (x, y) in cur_rock:
                board.add((x, y))
            highest_y = max(max_y, highest_y)
            break

    return board, highest_y, move_counter


def display_tetris(board, cur_rock = {}):
    max_y = 0
    for (_, y) in board:
        max_y = max(y, max_y)
    for (_, y) in cur_rock:
        max_y = max(y, max_y)

    for y in range(max_y, -1, -1):
        line = '|'
        for x in range(7):
            if (x, y) in board:
                line += '#'
            elif (x, y) in cur_rock:
                line += "@"
            else:
                line += '.'
        print(line + '|')
    print("+-------+")


def solve_part1(input: str) -> int:
    moves = input[:-1]
    highest_y = -1
    i = 0
    j = 0
    board = set()
    while i < 2022:
        board, highest_y, j = add_rock(board, moves, highest_y, i, j)
        i += 1
    return highest_y+1


def get_skyline(board):
    skyline = [0]*7
    for (x, y) in board:
        skyline[x] = max(y, skyline[x])
    skyline = [x-min(skyline) for x in skyline]
    return tuple(skyline)


def solve_part2(input: str) -> int:
    moves = input[:-1]
    highest_y = -1
    i = 0
    j = 0
    board = set()
    states = set()
    state_first_occured = {}
    period_start = period_length = 0
    while True:
        board, highest_y, j = add_rock(board, moves, highest_y, i, j)
        skyline = get_skyline(board)
        state = (i%len(SHAPES), j%len(moves), skyline)
        if state in states:
            period_start = state_first_occured[state][0]
            period_length = i - period_start
            period_height = highest_y - state_first_occured[state][1]
            break
        else:
            states.add(state)
            state_first_occured[state] = (i, highest_y)
        i += 1

    periods = (1000000000000-period_start) // period_length

    highest_y = -1
    i = 0
    j = 0
    board = set()
    while i < (1000000000000-(periods*period_length)):
        board, highest_y, j = add_rock(board, moves, highest_y, i, j)
        i += 1

    return highest_y + 1 + periods*period_height


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
