from binary_tree_task.binary_tree import BinaryTree

tree = BinaryTree()
tree_nodes = [8, 3, 10, 9, 1, 6, 8, 11, 4, 7, 14, 13, 20, 19, 19, 18, 22]

for node in tree_nodes:
    tree.insert(node)

print("Print binary tree by width:")
tree.traverse_in_width(print)

print("Print binary tree by depth:")
tree.traverse_in_depth(print)

if 4 in tree:
    tree.remove(4)
    print("Tree length after remove =", len(tree))

for node in tree:
    print("Node =", node)
