import math

puz = 265149
grid = {}
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
cur_dir = 0
nxt_dir = 1
cur_location = tuple([0, 0])
grid[cur_location] = 0
rev_grid = {}
rev_grid[0] = cur_location
for i in range(1, puz + 1):
    cur_location = tuple([sum(x) for x in zip(cur_location, directions[cur_dir])])
    grid[cur_location] = i
    rev_grid[i] = cur_location 
    left_loc = tuple([sum(x) for x in zip(cur_location, directions[nxt_dir])])
    if left_loc not in grid:
        cur_dir = (cur_dir + 1) % 4
        nxt_dir = (nxt_dir + 1) % 4

print(sum(map(abs, rev_grid[puz])) - 1)