from itertools import combinations
f = open('input.txt')
lines = []
for l in f.readlines():
    lines.append(map(int, l.split()))
n = []
for l in lines:
    for c in combinations(l, 2):
        d = sorted(c)
        if d[1] % d[0] == 0:
            n.append(d[1] / d[0])
            break
print(sum(n))


