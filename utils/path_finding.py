import sys
from queue import PriorityQueue


def example_grid_shortest_path(start, end, grid):
    to_visit = PriorityQueue()
    to_visit.put((0, start))
    visited = set()
    r = -1
    while not to_visit.empty() and r == -1:
        (cost, (x, y)) = to_visit.get()
        if (x, y) in visited:
            continue
        for (dx, dy) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < len(grid[y]) and 0 <= ny < len(grid):
                if grid[ny][nx] - grid[y][x] < 2:
                    if (nx, ny) == end:
                        r = cost + 1
                        break
                    if (nx, ny) not in visited:
                        to_visit.put((cost + 1, (nx, ny)))
        visited.add((x, y))

    return r


def graph_distance_table(graph, nodes=set()):
    if len(nodes) == 0:
        nodes = set(graph.keys())
    all_nodes = set(graph.keys())

    table = {}
    for start in nodes:
        dist = {}
        for n in all_nodes:
            if n != start:
                dist[n] = -1
        dist[start] = 0

        reachable = set([start])
        visited = set()
        to_visit = set(nodes)
        while len(to_visit) > 0:
            # Select next visiting node
            low = sys.maxsize
            node = None
            for n in reachable:
                if dist[n] < low:
                    low = dist[n]
                    node = n

            # Visit node
            cur_node = graph[node]
            cost = dist[node]
            for x in cur_node['neighbours']:
                if x not in visited:
                    if dist[x] == -1:
                        dist[x] = cost+1
                        reachable.add(x)
                    elif dist[x] > cost+1:
                        dist[x] = cost+1

            visited.add(node)
            reachable.remove(node)
            if node in to_visit:
                to_visit.remove(node)

        # Only save required nodes
        table[start] = {}
        for n in nodes:
            if n != start:
                table[start][n] = dist[n]

    return table