from node import Node
from binary_tree import BinaryTree

tree = BinaryTree(Node(9))
tree.__add__(Node(5))
tree.__add__(Node(11))
tree.__add__(Node(3))
tree.__add__(Node(6))

print(tree.head)
print(tree.head.left)
print(tree.head.left.left)
print(tree.head.left.right)
print(tree.head.right)
