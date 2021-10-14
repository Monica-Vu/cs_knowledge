def invert_binary_tree_recursive(root):
    if root: 
        root.left, root.right = invert_binary_tree_recursive(root.right), invert_binary_tree_recursive(root.left)
        return root 