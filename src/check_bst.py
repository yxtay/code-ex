def check_bst(root, min_value=0, max_value=10 ** 4):
    if root is None:
        return True

    valid = min_value < root.data and root.data < max_value
    valid = valid and check_bst(root.left, min_value, root.data)
    valid = valid and check_bst(root.right, root.data, max_value)

    return valid
