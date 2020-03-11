"""from anytree import Node, RenderTree, find_by_attr

with open('tree_raw.txt', 'r') as f:
    lines = f.readlines()[1:]
    root = Node(lines[0].split(" ")[0])

    for line in lines:
        line = line.split(" ")
        Node("".join(line[1:]).strip(), parent=find_by_attr(root, line[0]))

    for pre, _, node in RenderTree(root):
        print("%s%s" % (pre, node.name))"""

from anytree import Node, RenderTree, find_by_attr

with open('tree_raw.txt', 'r') as f:
    lines = f.readlines()[1:]
    root = Node(lines[0].split(" ")[0])
    nodes = {}
    nodes[root.name] = root

    for line in lines:
        line = line.split(" ")
        name = "".join(line[1:]).strip()
        nodes[name] = Node(name, parent=nodes[line[0]])

    for pre, _, node in RenderTree(root):
        print("%s%s" % (pre, node.name))