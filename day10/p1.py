f = open('input.txt')
skip_size = 0
cur_pos = 0
lens = map(int, f.read().split(","))
nums = list(range(256))
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

print(nums[0] * nums[1])