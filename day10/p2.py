from functools import reduce
f = open('input.txt')
skip_size = 0
cur_pos = 0
instr = f.read()
lens = [ord(c) for c in instr]
lens.extend([17, 31, 73, 47, 23])
nums = list(range(256))
for r in range(64):
    for l in lens:
        start = cur_pos
        end = start + l
        # reverse
        for i in range(l/2):
            b = (end - i - 1) % len(nums)
            a = (start + i) % len(nums)
            temp = nums[a]
            nums[a] = nums[b]
            nums[b] = temp
        # adjust cur
        cur_pos = cur_pos + l + skip_size
        skip_size += 1

dense = []
for i in range(16):
    block = nums[i * 16: (i + 1) * 16]
    x = reduce(lambda a, b: a ^ b, block, 0)
    dense.append(x)
    
print("".join([format(d, "02X") for d in dense]))
