from collections import deque
f = open('input.txt')
steps = f.read().split(",")
progs = deque([chr(o) for o in range(ord("a"), ord("a") + 16)])
for s in steps:
    if s[0] == "s":
        progs.rotate(int(s[1:]))
    elif s[0] == "x":
        a, b = map(int, s[1:].split("/"))
        tmp = progs[a]
        progs[a] = progs[b]
        progs[b] = tmp
    elif s[0] == "p":
        a_n, b_n = s[1:].split("/")
        a = progs.index(a_n)
        b = progs.index(b_n)
        tmp = progs[a]
        progs[a] = progs[b]
        progs[b] = tmp

print("".join(progs))