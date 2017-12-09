from collections import deque
f = open('input.txt')
stack = deque()
ignore = False
garbage = 0
s = f.read()
for c in s:
    if ignore:
        ignore = False
        continue
    if c == "!":
        ignore = True
    elif c == "{":
        if len(stack) == 0:
            stack.append(c)
        if stack[-1] == "<":
            garbage += 1
    elif c == "}":
        if stack[-1] == "<":
            garbage += 1
    elif c == "<":
        if len(stack) == 0:
            stack.append(c)
        elif len(stack) > 0 and stack[-1] != "<":
            stack.append(c)
        elif stack[-1] == "<":
            garbage += 1
    elif c == ">":
        if len(stack) > 0 and stack[-1] == "<":
            stack.pop()
    else:
        if stack[-1] == "<":
            garbage += 1

print(garbage)

