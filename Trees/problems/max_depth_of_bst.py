"""
Question: 
Given the root of a binary tree, return its maximum depth. 

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

(1) Assumptions 
```
class Node:
    def __init__(value):
        self.value = value
        self.left = None
        self.right = None 
```

(2) Contraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100

Test Cases:
- Empty Tree / Root is None 
- Left and right subtree has the same depth 
- Left subtree's depth is more than right subtree
- Right subtree's depth is more than left subtree
- Skewed trees (for performance purposes)

Question Source:
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

"""

"""
def max_depth_bst_recursive(root):
    if root is None:
        return 0
    
    return 1 + max(max_depth_bst_recursive(root.left), max_depth_bst_recursive(root.right))

"""
Algorithm Explanation: 
- At every level, the queue is a list of node at the given level. We increase the depth until the queue is an empty list.
- Insteading of removing or popping, reset the list to make it more efficient.

Time Complexity: O(n) the
Space Complexity: O(log n) -- worst case is that we store each level 
"""
def max_depth_bst_iterative(root): 
    if root is None:
        return 0 

    depth = 0
    level = [root]

    while level:
        depth += 1 
        queue = [] 

        for ele in level:
            if ele.left:
                queue.append(ele.left)
            if ele.right:
                queue.append(ele.right)
        level = queue
    
    return depth 