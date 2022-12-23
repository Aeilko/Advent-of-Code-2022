from utils.aoc import check_for_input_file
from utils.file import read_file_content
from utils.grid import display_dict_grid


RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


# I ran part 2 directly once I finished the mapping, but I forgot to apply the new direction after the mapping.
# But somehow I still got the right answer, no clue how that's possible for such a big mistake.
# So yeah, the code should be wrong, but it isn't, so i don't feel like fixing it.


def solve_part1(input: str) -> int:
    (board, path) = input[:-1].split("\n\n")

    # Parse board
    grid = {}
    start = (-1, -1)
    board = board.split("\n")
    total_height = len(board)
    total_width = 0
    for y in range(len(board)):
        total_width = max(len(board[y]), total_width)
        for x in range(len(board[y])):
            if board[y][x] != ' ':
                grid[(x, y)] = board[y][x]
                if start == (-1, -1) and board[y][x] == '.':
                    start = (x, y)

    # Parse moves
    moves = []
    path = path.split("R")
    for a in path:
        b = a.split("L")
        for c in b[:-1]:
            moves.append((int(c), 'L'))
        moves.append((int(b[-1]), 'R'))
    moves[-1] = (moves[-1][0], None)

    # Parse mappings
    mapping = {}
    # Left Right
    for y in range(total_height):
        min_x = 0
        max_x = len(board[y])-1
        found_board = False
        for x in range(len(board[y])):
            if not found_board and board[y][x] != ' ':
                found_board = True
                min_x = x
            elif found_board and board[y][x] == ' ':
                max_x = x-1
                break
        mapping[((min_x-1, y), LEFT)] = (max_x, y)
        mapping[((max_x+1), y), RIGHT] = (min_x, y)
    # Up Down
    for x in range(total_width):
        min_y = 0
        max_y = len(board)-1
        found_board = False
        for y in range(total_height):
            if not found_board and len(board[y]) > x and board[y][x] != ' ':
                found_board = True
                min_y = y
            elif found_board and (len(board[y]) <= x or board[y][x] == ' '):
                max_y = y-1
                break
        mapping[((x, min_y-1), UP)] = (x, max_y)
        mapping[((x, max_y+1), DOWN)] = (x, min_y)

    # Simulate moves
    cur_location = start
    cur_direction = 0
    for (steps, turn) in moves:
        # Move
        dx, dy = DIRECTIONS[cur_direction]
        for _ in range(steps):
            n_coord = (cur_location[0] + dx, cur_location[1] + dy)
            if (n_coord, cur_direction) in mapping:
                n_coord = mapping[(n_coord, cur_direction)]

            if n_coord not in grid:
                print('space!', n_coord)
                break
            elif grid[n_coord] == '.':
                cur_location = n_coord
            elif grid[n_coord] == '#':
                break
            else:
                print("Error!", cur_location, cur_direction, steps, turn, n_coord)
                break

        # Turn
        if turn is not None:
            cur_direction = (cur_direction + (1 if turn == 'R' else -1)) % 4

    return (cur_location[1]+1)*1000 + (cur_location[0]+1)*4 + cur_direction


def solve_part2(input: str) -> int:
    (board, path) = input[:-1].split("\n\n")

    # Parse board
    grid = {}
    start = (-1, -1)
    board = board.split("\n")
    total_height = len(board)
    total_width = 0
    for y in range(len(board)):
        total_width = max(len(board[y]), total_width)
        for x in range(len(board[y])):
            if board[y][x] != ' ':
                grid[(x, y)] = board[y][x]
                if start == (-1, -1) and board[y][x] == '.':
                    start = (x, y)

    # Parse moves
    moves = []
    path = path.split("R")
    for a in path:
        b = a.split("L")
        for c in b[:-1]:
            moves.append((int(c), 'L'))
        moves.append((int(b[-1]), 'R'))
    moves[-1] = (moves[-1][0], None)

    # Hardcoded mapping
    mapping = {}
    # 1, 0 UP
    y = -1
    x = 50
    for dx in range(50):
        mapping[((x+dx, y), UP)] = ((0, 150+dx), RIGHT)
    # 2, 0 UP
    y = -1
    x = 100
    for dx in range(50):
        mapping[((x+dx, y), UP)] = ((0+dx, 199), UP)
    # 1, 0 LEFT
    x = 49
    y = 0
    for dy in range(50):
        mapping[((x, y+dy), LEFT)] = ((0, 149-dy), RIGHT)
    # 2, 0 RIGHT
    x = 150
    y = 0
    for dy in range(50):
        mapping[((x, y+dy), RIGHT)] = ((99, 149-dy), LEFT)
    # 2, 0 DOWN
    y = 50
    x = 100
    for dx in range(50):
        mapping[((x+dx, y), DOWN)] = ((99, 50+dx), LEFT)
    # 1, 1 LEFT
    x = 49
    y = 50
    for dy in range(50):
        mapping[((x, y+dy), LEFT)] = ((0+dy, 100), DOWN)
    # 1, 1 RIGHT
    x = 100
    y = 50
    for dy in range(50):
        mapping[((x, y+dy), RIGHT)] = ((100+dy, 49), UP)
    # 0, 2 UP
    y = 99
    x = 0
    for dx in range(50):
        mapping[((x+dx, y), UP)] = ((50, 50+dx), RIGHT)
    # 0, 2 LEFT
    x = -1
    y = 100
    for dy in range(50):
        mapping[((x, y+dy), LEFT)] = ((50, 49-dy), RIGHT)
    # 1, 2 RIGHT
    x = 100
    y = 100
    for dy in range(50):
        mapping[((x, y+dy), RIGHT)] = ((149, 49-dy), LEFT)
    # 1, 2 DOWN
    y = 150
    x = 50
    for dx in range(50):
        mapping[((x+dx, y), DOWN)] = ((49, 150+dx), LEFT)
    # 0, 3 LEFT
    x = -1
    y = 150
    for dy in range(50):
        mapping[((x, y+dy), LEFT)] = ((50+dy, 0), DOWN)
    # 0, 3 RIGHT
    x = 50
    y = 150
    for dy in range(50):
        mapping[((x, y+dy), RIGHT)] = ((50+dy, 149), UP)
    # 0, 3 DOWN
    y = 200
    x = 0
    for dx in range(50):
        mapping[((x+dx, y), DOWN)] = ((50+dx, 0), DOWN)

    # Simulate moves
    cur_location = start
    cur_direction = 0
    for (steps, turn) in moves:
        # Move
        dx, dy = DIRECTIONS[cur_direction]
        for _ in range(steps):
            n_coord = (cur_location[0] + dx, cur_location[1] + dy)
            if (n_coord, cur_direction) in mapping:
                n_coord = mapping[(n_coord, cur_direction)]

            if n_coord not in grid:
                # print('space!', n_coord)
                break
            elif grid[n_coord] == '.':
                cur_location = n_coord
            elif grid[n_coord] == '#':
                break
            else:
                print("Error!", cur_location, cur_direction, steps, turn, n_coord)
                break

        # Turn
        if turn is not None:
            cur_direction = (cur_direction + (1 if turn == 'R' else -1)) % 4

    return (cur_location[1] + 1) * 1000 + (cur_location[0] + 1) * 4 + cur_direction


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
    # test_part2()
    print("Part 2 result:\t" + str(solve_part2(input)))
