import re
f = open('input.txt')
zero_set = set()
lines = f.readlines()
def add_line(line):
    from_node, to_nodes = line.split("<->")
    to_node_list = to_nodes.split(",")
    zero_set.add(from_node.strip())
    zero_set.update([n.strip() for n in to_node_list])

line_one = lines.pop(0)
add_line(line_one)
zero_size = -1
while True:
    remove_line = None
    for l in lines:
        from_node, to_nodes = l.split("<->")
        if from_node.strip() in zero_set:
            add_line(l)
            remove_line = l
            break
    if remove_line:
        lines.remove(remove_line)
    else:
        break

print(len(zero_set))


