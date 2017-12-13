f = open('input.txt')
wall = {}
depths = {}
for l in f.readlines():
    layer, depth = [int(x.strip()) for x in l.split(":")]
    wall[layer] = 1 if depth == 1 else (depth - 1) * 2
    depths[layer] = depth
num_steps = max(wall.keys())
offset = 0
while True:
    sev = 0
    bad = False
    for s in range(0, num_steps + 1):
        if s in wall and (s + offset) % wall[s] == 0:
            bad = True
            break
    if bad:
        offset += 1
        continue
    if sev == 0 and not bad:
        print(offset)
        break
