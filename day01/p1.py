f = open('input.txt')
instr = f.read()
num_list = [int(n) for n in instr]
add_nums = []
for i in range(len(num_list) - 1):
    if (num_list[i] == num_list[i+1]):
        add_nums.append(num_list[i])
if num_list[0] == num_list[-1]:
    add_nums.append(num_list[0])
print(sum(add_nums))


