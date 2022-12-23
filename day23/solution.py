from utils.aoc import check_for_input_file
from utils.file import read_file_content
from utils.grid import display_dict_grid, dict_grid_min_max


def parse_input(lines):
    grid = {}
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == '#':
                grid[(x, y)] = '#'

    return grid


def perform_round(grid, moves_list):
    want_to_move = 0
    planned_moves = {}

    # Check for each plant if they want to move
    for (x, y) in grid:
        if get_num_neighbours(x, y, grid) > 0:
            want_to_move += 1
            for (dx, dy) in moves_list:
                n = 0
                for do in [-1, 0, 1]:
                    if dx == 0:
                        if (x + do, y + dy) not in grid:
                            n += 1
                    else:
                        if (x + dx, y + do) not in grid:
                            n += 1
                if n == 3:
                    planned_moves[(x, y)] = (x + dx, y + dy)
                    break

    # Count the occurrences of the destinations
    dest_count = {}
    for dest in planned_moves.values():
        if dest in dest_count:
            dest_count[dest] += 1
        else:
            dest_count[dest] = 1

    # Move if you are the only one to move to the new field
    for (x, y) in planned_moves:
        (nx, ny) = planned_moves[(x, y)]
        if dest_count[(nx, ny)] == 1:
            del grid[(x, y)]
            grid[(nx, ny)] = '#'

    # Rotate the moves
    moves_list.append(moves_list.pop(0))

    return grid, moves_list, want_to_move


def get_num_neighbours(x, y, grid):
    r = 0
    for (dx, dy) in [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]:
        if (x+dx, y+dy) in grid:
            r += 1
    return r


def solve_part1(input: str) -> int:
    lines = input[:-1].split("\n")
    grid = parse_input(lines)

    moves_list = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    rounds = 0
    while rounds < 10:
        grid, moves_list, _ = perform_round(grid, moves_list)
        rounds += 1

    min_x, max_x, min_y, max_y = dict_grid_min_max(grid)
    return ((abs(max_x-min_x)+1) * (abs(max_y-min_y)+1)) - len(grid)


def solve_part2(input: str) -> int:
    lines = input[:-1].split("\n")
    grid = parse_input(lines)

    moves_list = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    want_to_move = 1
    rounds = 0
    while want_to_move > 0:
        grid, moves_list, want_to_move = perform_round(grid, moves_list)
        rounds += 1

    return rounds


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
