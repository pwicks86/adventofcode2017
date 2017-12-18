from collections import defaultdict
f = open('input.txt')
inst = f.readlines()
# inst = """set a 1
# add a 2
# mul a a
# mod a 5
# snd a
# set a 0
# rcv a
# jgz a -1
# set a 1
# jgz a -2""".splitlines()

ip = 0
registers = defaultdict(int)
freq = 0

def val(x):
    try:
        xi = int(x.strip())
        return xi
    except:
        return registers[x]

while True:
    if ip < 0 or ip > len(inst):
        break
    i = inst[ip].split()
    offset = 1
    if i[0] == "snd":
        freq = val(i[1])
    elif i[0] == "set":
        registers[i[1]] = val(i[2])
    elif i[0] == "add":
        registers[i[1]] += val(i[2])
    elif i[0] == "mul":
        registers[i[1]] *= val(i[2])
    elif i[0] == "mod":
        registers[i[1]] %= val(i[2])
    elif i[0] == "rcv":
        if val(i[1]) > 0:
            if freq != 0:
                print(freq)
                break
    elif i[0] == "jgz":
        if val(i[1]) > 0:
            offset = val(i[2])
    ip += offset
