import sys


def display_dict_grid(grid):
    minx, maxx, miny, maxy = dict_grid_min_max(grid)

    for y in range(miny, maxy+1):
        line = ""
        for x in range(minx, maxx+1):
            if (x,y) in grid:
                line += grid[(x, y)]
            else:
                line += "."
        print(line)


def dict_grid_min_max(grid):
    minx = miny = sys.maxsize
    maxx = maxy = sys.maxsize * -1
    for (x, y) in grid:
        minx = x if x < minx else minx
        maxx = x if x > maxx else maxx
        miny = y if y < miny else miny
        maxy = y if y > maxy else maxy

    return minx, maxx, miny, maxy
