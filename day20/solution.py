from utils.aoc import check_for_input_file
from utils.file import read_file_content
from utils.linked_list import LinkedList


def get_node_x_forward(node, x, length):
    steps = x % length
    for _ in range(steps):
        node = node.next
    return node


def llist_to_string(n):
    start_val = n.val
    r = [n.val]
    n = n.next
    while n.val != start_val:
        r.append(n.val)
        n = n.next
    return str(r)


def solve_part1(input: str) -> int:
    nums = [int(x) for x in input[:-1].split("\n")]
    length = len(nums)
    llist = LinkedList(nums)
    items = list(llist.list)
    # Create circle
    llist.list[-1].next = llist.list[0]

    zero_node = llist.values[0]

    for cur_node in items:
        if cur_node.val != 0:
            # We remove the item, so modulo length-1, but only if we move more than one full cycle
            steps = cur_node.val if 0 < cur_node.val < length else cur_node.val % (length - 1)
            if steps != 0:
                # Remove current item from list
                prev_node = get_node_x_forward(cur_node, -1, length)
                next_node = cur_node.next
                prev_node.next = next_node

                # Find new prev and next node
                new_prev_node = get_node_x_forward(cur_node, steps, length)
                new_next_node = new_prev_node.next

                # Save node in new position
                new_prev_node.next = cur_node
                cur_node.next = new_next_node

    return sum([get_node_x_forward(zero_node, x, length).val for x in [1000, 2000, 3000]])


def solve_part2(input: str) -> int:
    nums = [int(x)*811589153 for x in input[:-1].split("\n")]
    length = len(nums)
    llist = LinkedList(nums)
    items = list(llist.list)
    # Create circle
    llist.list[-1].next = llist.list[0]

    zero_node = llist.values[0]

    for _ in range(10):
        for cur_node in items:
            if cur_node.val != 0:
                # We remove the item, so modulo length-1, but only if we move more than one full cycle
                steps = cur_node.val if 0 < cur_node.val < length else cur_node.val % (length - 1)
                if steps != 0:
                    # Remove current item from list
                    prev_node = get_node_x_forward(cur_node, -1, length)
                    next_node = cur_node.next
                    prev_node.next = next_node

                    # Find new prev and next node
                    new_prev_node = get_node_x_forward(cur_node, steps, length)
                    new_next_node = new_prev_node.next

                    # Save node in new position
                    new_prev_node.next = cur_node
                    cur_node.next = new_next_node

    return sum([get_node_x_forward(zero_node, x, length).val for x in [1000, 2000, 3000]])




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
