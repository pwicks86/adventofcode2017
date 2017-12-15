f = open('input.txt')
a = int(f.readline().split(" ")[-1])
b = int(f.readline().split(" ")[-1])
a_factor = 16807
b_factor = 48271
divider = 2147483647

def gen_val(v, factor):
    return (v * factor) % divider

count = 0
for i in range(5000000):
    while True:
        a = gen_val(a, a_factor)
        if a % 4 == 0:
            break
    while True:
        b = gen_val(b, b_factor)
        if b % 8 == 0:
            break
    if ((a & 0xFFFF) == (b & 0xFFFF)):
        count += 1
print(count)
