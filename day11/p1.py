f = open('input.txt')
steps = f.read().split(",")
x = 0
y = 0
z = 0
for s in steps:
    if s == "n":
        y += 1
        z -= 1
    elif s == "s":
        y -= 1
        z += 1
    elif s == "nw":
        y += 1
        x -= 1
    elif s == "ne":
        x += 1
        z -= 1
    elif s == "se":
        y -= 1
        x += 1
    elif s == "sw":
        z += 1
        x -= 1
    
print(max(x,y,z))