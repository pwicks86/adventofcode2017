import copy
from collections import deque
f = open('input.txt')
steps = f.read().split(",")
progs = deque([chr(o) for o in range(ord("a"), ord("a") + 16)])
orig = copy.deepcopy(progs)

def dance(p):
    ps = "".join(p)
    for s in steps:
        if s[0] == "s":
            p.rotate(int(s[1:]))
        elif s[0] == "x":
            a, b = map(int, s[1:].split("/"))
            tmp = p[a]
            p[a] = p[b]
            p[b] = tmp
        elif s[0] == "p":
            a_n, b_n = s[1:].split("/")
            a = p.index(a_n)
            b = p.index(b_n)
            tmp = p[a]
            p[a] = p[b]
            p[b] = tmp
    return p

num_to_do = int(10e9)
for i in range(num_to_do):
    progs = dance(progs)
    if progs == orig:
        cycle = i + 1
        end_num = num_to_do % cycle
        break
progs = orig
for i in range(end_num):
    progs = dance(progs)

print("".join(progs))
