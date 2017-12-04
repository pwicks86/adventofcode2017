from collections import Counter
f = open('input.txt')
valid = 0
for l in f.readlines():
    words = l.split()
    c = Counter(words)
    if c.most_common(1)[0][1] == 1:
        valid += 1
print(valid)


    
