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