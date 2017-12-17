puz = 377
pos = 0
zero_pos = 0
buflen = 1
after_zero = -1
for i in range(1, 50000000 + 1):
    pos = (pos + puz) % buflen
    if pos < zero_pos or pos == buflen:
        zero_pos += 1
    if pos == zero_pos:
        after_zero = i
    buflen += 1
    pos = (pos + 1) % buflen
print(after_zero)
