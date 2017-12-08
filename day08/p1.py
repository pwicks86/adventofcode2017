import re
from operator import add, sub
from collections import defaultdict
f = open('input.txt')
registers = defaultdict(int)
for l in f.readlines():
    m = re.match("(\w+)\s+(\w+)\s+(-?\d+) if (\w+) (.*)", l)
    g = m.groups()
    register = g[0]
    reg_op = add if g[1] == 'inc' else sub 
    amount = int(g[2])
    truth_str = "registers['%s'] %s" % (g[3], g[4])
    if (eval(truth_str)):
        registers[register] = reg_op(registers[register], amount)

print(max(registers.values()))