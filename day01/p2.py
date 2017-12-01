f = open('input.txt')
instr = f.read()
num_list = [int(n) for n in instr]
add_nums = []
for i in range(len(num_list) - 1):
    p = (i + (len(num_list) / 2)) % len(num_list)
    if (num_list[i] == num_list[p]):
        add_nums.append(num_list[i])
if num_list[-1] == num_list[(len(num_list) / 2) - 1]:
    add_nums.append(num_list[-1])
print(sum(add_nums))



