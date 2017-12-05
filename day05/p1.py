f = open('input.txt')
instructions = [int(i) for i in f.readlines()]
num_inst = len(instructions)
cur_pos = 0
steps = -1
while True:
    steps += 1
    try:
        cur_val = instructions[cur_pos]
        instructions[cur_pos] += 1
        cur_pos += cur_val
    except:
        print(steps)
        break
