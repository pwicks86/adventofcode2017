f = open('input.txt')
a = int(f.readline().split(" ")[-1])
b = int(f.readline().split(" ")[-1])
a_factor = 16807
b_factor = 48271
divider = 2147483647

def gen_val(v, factor):
    return (v * factor) % divider

count = 0
for i in range(40000000):
    a = gen_val(a, a_factor)
    b = gen_val(b, b_factor)
    if ((a & 0xFFFF) == (b & 0xFFFF)):
        count += 1
print(count)