puz = 265149
grid = {}
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
cur_dir = 0
nxt_dir = 1
cur_location = tuple([0, 0])
grid[cur_location] = 1
for i in range(1, puz + 1):
    cur_location = tuple([sum(x) for x in zip(cur_location, directions[cur_dir])])
    val = 0
    for xdiff in range(-1, 2, 1):
        for ydiff in range(-1, 2, 1):
            if xdiff == 0 and ydiff == 0:
                continue
            check_location = (cur_location[0] + xdiff, cur_location[1] + ydiff)
            if check_location in grid:
                val += grid[check_location]

    if val > puz:
        print(val)
        break
    grid[cur_location] = val
    left_loc = tuple([sum(x) for x in zip(cur_location, directions[nxt_dir])])
    if left_loc not in grid:
        cur_dir = (cur_dir + 1) % 4
        nxt_dir = (nxt_dir + 1) % 4