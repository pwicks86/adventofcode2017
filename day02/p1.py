f = open('input.txt')
lines = []
for l in f.readlines():
    lines.append(map(int, l.split()))
checksum = []
for l in lines:
    lsorted = sorted(l)
    checksum.append(abs(lsorted[0] - lsorted[-1]))

print(sum(checksum))

