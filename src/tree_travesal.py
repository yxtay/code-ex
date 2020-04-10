class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.value)
        in_order(node.right)


def pre_order(node):
    if node is not None:
        print(node.value)
        in_order(node.left)
        in_order(node.right)


def post_order(node):
    if node is not None:
        in_order(node.left)
        in_order(node.right)
        print(node.value)
