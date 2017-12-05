f = open('input.txt')
instructions = [int(i) for i in f.readlines()]
num_inst = len(instructions)
cur_pos = 0
steps = -1
while True:
    steps += 1
    try:
        cur_val = instructions[cur_pos]
        if cur_val >= 3:
            instructions[cur_pos] -= 1
        else:
            instructions[cur_pos] += 1

        cur_pos += cur_val
    except:
        print(steps)
        break

