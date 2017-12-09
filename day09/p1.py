from collections import deque
f = open('input.txt')
stack = deque()
ignore = False
score = 0
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
        elif stack[-1] != "<":
            stack.append(c)
    elif c == "}":
        if stack[-1] == "{":
            stack.pop()
            score += 1 + len(stack)
        elif stack[-1] == "<":
            pass
    elif c == "<":
        if stack[-1] != "<":
            stack.append(c)
    elif c == ">":
        if stack[-1] == "<":
            stack.pop()

print(score)
