class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def lowest_common_ancester(root, v1, v2):
    if root is None:
        return root

    if v1 < root.info and v2 < root.info:
        return lowest_common_ancester(root.left, v1, v2)
    elif v1 > root.info and v2 > root.info:
        return lowest_common_ancester(root.right, v1, v2)
    else:
        return root
