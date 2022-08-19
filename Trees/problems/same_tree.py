"""
Question:
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Assumptions:
(1) We're given the implementation of the `Node` class: 

```
class Node:
    def __init__(value):
        self.value = value
        self.left = None
        self.right = None 
```

Test Cases:
- Both trees are empty
- p is an empty tree and q is not empty 
- q is an empty tree and p is not empty 
- p and q are identical except p is missing one leaf node 
- p and q are identical except q is missing one leaf node 
- p and q are identical except q is missing one leaf node are identical 

Time Complexity: O(n) --> need to visit all nodes 
Space Complexity: O(h) or O(n) for skewed --> need to store function call stack 

"""

def is_same_tree(p, q):
    if p is None and q is None:
        return True
    
    elif (p is None) or (q is None):
        return False 
    
    return (p.value == q.value) and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)