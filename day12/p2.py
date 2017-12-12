
import re
f = open('input.txt')
set_list = []
set_list.append(set())
lines = f.readlines()
def add_line(line, s):
    from_node, to_nodes = line.split("<->")
    to_node_list = to_nodes.split(",")
    s.add(from_node.strip())
    s.update([n.strip() for n in to_node_list])

line_one = lines.pop(0)
add_line(line_one, set_list[0])

while True:
    if len(lines) == 0:
        break
    remove_line = None
    for l in lines:
        from_node, to_nodes = l.split("<->")
        if from_node.strip() in set_list[-1]:
            add_line(l, set_list[-1])
            remove_line = l
            break
    if remove_line:
        lines.remove(remove_line)
    else:
        set_list.append(set())
        line_one = lines.pop(0)
        add_line(line_one, set_list[-1])

print(len(set_list))



