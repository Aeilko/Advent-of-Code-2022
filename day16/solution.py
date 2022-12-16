from utils.aoc import check_for_input_file
from utils.file import read_file_content
from utils.path_finding import graph_distance_table


def parse_input(lines):
    graph = {}
    flow_valves = set()
    for line in lines:
        # Valve XB has flow rate=0; tunnels lead to valves WZ, LE
        (valve, tunnels) = line[6:].split(";")
        parts = valve.split(" has flow rate=")
        name = parts[0]
        flow = int(parts[1])
        tunnels = tunnels.split("valve ")[-1]
        tunnels = tunnels.split("valves ")[-1]
        tunnels = tunnels.split(", ")
        graph[name] = {
            'flow': flow,
            'neighbours': tunnels,
            'open': False,
        }
        if flow > 0:
            flow_valves.add(name)
    return graph, flow_valves


def find_max_score(cur_node, to_visit, graph, distance, score_pm, rem_time):
    r = 0
    if graph[cur_node]['flow'] > 0:
        r += score_pm
        rem_time -= 1
        score_pm += graph[cur_node]['flow']

    max_score = rem_time*score_pm
    for x in to_visit:
        if rem_time - distance[cur_node][x] > 1:
            tmp = set(to_visit)
            tmp.remove(x)
            s = score_pm * distance[cur_node][x]
            s += find_max_score(x, tmp, graph, distance, score_pm, rem_time-distance[cur_node][x])
            if s > max_score:
                max_score = s

    return r + max_score


def find_max_score_2(p_node, e_node, p_travel, e_travel, to_visit, graph, distance, score_pm, rem_time):
    if rem_time < 1:
        return 0

    if p_travel == 0:
        score_pm += graph[p_node]['flow']

        max_score = rem_time * score_pm
        visited = False
        for x in to_visit:
            if rem_time - distance[p_node][x] > 1:
                visited = True
                tmp = set(to_visit)
                tmp.remove(x)
                p_travel = distance[p_node][x] + 1
                time = min(p_travel, e_travel, rem_time)
                s = score_pm * time
                s += find_max_score_2(x, e_node, p_travel-time, e_travel-time, tmp, graph, distance, score_pm, rem_time-time)
                if s > max_score:
                    max_score = s

        if not visited and e_travel <= rem_time:
            # P cant open any valves, but E can
            p_travel = rem_time+1
            time = e_travel
            s = score_pm * time
            s += find_max_score_2(p_node, e_node, p_travel - time, e_travel - time, to_visit, graph, distance, score_pm, rem_time - time)
            if s > max_score:
                max_score = s
    elif e_travel == 0:
        score_pm += graph[e_node]['flow']

        max_score = rem_time * score_pm
        visited = False
        for x in to_visit:
            if rem_time - distance[e_node][x] > 1:
                visited = True
                tmp = set(to_visit)
                tmp.remove(x)
                e_travel = distance[e_node][x] + 1
                time = min(p_travel, e_travel, rem_time)
                s = score_pm * time
                s += find_max_score_2(p_node, x, p_travel-time, e_travel-time, tmp, graph, distance, score_pm, rem_time-time)
                if s > max_score:
                    max_score = s

        if not visited and e_travel <= rem_time:
            # E cant open any valves, but P can
            e_travel = rem_time+1
            time = p_travel
            s = score_pm * time
            s += find_max_score_2(p_node, e_node, p_travel - time, e_travel - time, to_visit, graph, distance, score_pm, rem_time - time)
            if s > max_score:
                max_score = s

    return max_score


def solve_part1(input: str) -> int:
    lines = input[:-1].split("\n")

    graph, flow_valves = parse_input(lines)
    tmp = set(flow_valves)
    tmp.add("AA")
    table = graph_distance_table(graph, tmp)

    return find_max_score("AA", flow_valves, graph, table, 0, 30)


def solve_part2(input: str) -> int:
    lines = input[:-1].split("\n")

    graph, flow_valves = parse_input(lines)
    tmp = set(flow_valves)
    tmp.add("AA")
    table = graph_distance_table(graph, tmp)

    return find_max_score_2("AA", "AA", 0, 0, flow_valves, graph, table, 0, 25)


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
