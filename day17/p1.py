puz = 377
buf = [0]
pos = 0
for i in range(1, 2017 + 1):
    pos = (pos + puz) % len(buf)
    buf.insert(pos + 1, i)
    pos = (pos + 1) % len(buf)
x = buf.index(2017)
print(buf[x+1])