f = open('input.txt')
wall = {}
depths = {}
for l in f.readlines():
    layer, depth = [int(x.strip()) for x in l.split(":")]
    wall[layer] = 1 if depth == 1 else (depth - 1) * 2
    depths[layer] = depth
num_steps = max(wall.keys())
sev = 0
for s in range(0, num_steps + 1):
    if s in wall and s % wall[s] == 0:
        sev += s * depths[s]
print(sev)
