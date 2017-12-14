from functools import reduce
def knot_hash(s):
    skip_size = 0
    cur_pos = 0
    lens = [ord(c) for c in s]
    lens.extend([17, 31, 73, 47, 23])
    nums = list(range(256))
    for r in range(64):
        for l in lens:
            start = cur_pos
            end = start + l
            # reverse
            for i in range(l/2):
                b = (end - i - 1) % len(nums)
                a = (start + i) % len(nums)
                temp = nums[a]
                nums[a] = nums[b]
                nums[b] = temp
            # adjust cur
            cur_pos = cur_pos + l + skip_size
            skip_size += 1

    dense = []
    for i in range(16):
        block = nums[i * 16: (i + 1) * 16]
        x = reduce(lambda a, b: a ^ b, block, 0)
        dense.append(x)
        
    return "".join(("{:08b}".format(b) for b in dense))

instr = "ugkiagan"
grid = []
for i in range(128):
    hashstr = instr + "-" + str(i)
    hashed = knot_hash(hashstr)
    grid.append(hashed)

count = 0
visit_grid = {}
all_visited = set()
for row in range(128):
    for col in range(128):
        if grid[row][col] == "1" and (row,col) not in all_visited:
            count += 1
            queue = [(row,col)]
            while len(queue) > 0:
                r,c = queue.pop()
                if 0 <= r < 128 and 0 <= c < 128:
                    if (r,c) not in all_visited and grid[r][c] == "1":
                        all_visited.add((r,c))
                        queue.extend([(r+1, c), (r - 1, c), (r, c + 1), (r, c - 1)])

print(count)