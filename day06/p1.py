f = open('input.txt')
banks = [int(b) for b in f.read().split()]
seen = set()
seen.add(tuple(banks))
cycles = 0
while True:
    max_index = banks.index(max(banks))
    max_val = banks[max_index]
    banks[max_index] = 0
    for i in range(max_index + 1, max_index + max_val + 1):
        pos = i % len(banks)
        banks[pos] = banks[pos] + 1
    cycles += 1
    t = tuple(banks)
    if t in seen:
        print(cycles)
        break
    else:
        seen.add(t)