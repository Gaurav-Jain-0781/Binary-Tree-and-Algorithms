from node import Node


class BinaryTree:
    def __init__(self, head: Node):
        self.head = head

    def __add__(self, new_node: Node):
        current_node = self.head
        while current_node:
            if current_node == new_node:
                raise ValueError("such node already exist in the tree . ")
            elif current_node.value > new_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break
            elif current_node.value < new_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break
