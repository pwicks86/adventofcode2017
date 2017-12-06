f = open('input.txt')
banks = [int(b) for b in f.read().split()]
# banks = [0, 2, 7, 0]
seen = {}
seen[tuple(banks)] = 1
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
        print(seen[t])
        break
    else:
        for k in seen.keys():
            seen[k] += 1
        seen[t] = 1