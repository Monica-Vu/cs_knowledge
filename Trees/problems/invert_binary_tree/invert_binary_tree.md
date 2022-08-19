# Problem 
Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

**Constraints:**
* The number of nodes in the tree is in the range [0, 100].
* -100 <= Node.val <= 100

# Brainstorm
* When we say invert a binary tree, we mean flip the positions of it. For example, we would flip the positions of the leftmost child and the right most child. Then we would flip the second leftmost child and flip the second rightmost child. 
* In Python, we can swap these positions

# Code 
```
def invert_binary_tree_recursive(root):
    if root: 
        root.left, root.right = invert_binary_tree_recursive(root.right), invert_binary_tree_recursive(root.left)
        return root 
```

# Test Cases
* Empty Tree
* Tree only only one node
* Tree has three nodes and the leaves have the same value (tree is symmetrical)
* Tree is asymmetrical 
* Tree is symmetrical but contains different values
* Left-skewed Tree
* Right-skewed Tree
* A tree with lots of nodes (performance)

# Analysis 
Time Complexity: O(n) -> need to visit every node and flip it. 
Space Complexity: O(1) -> no need to store anytime technically 

# Sources
https://leetcode.com/problems/invert-binary-tree/
https://leetcode.com/problems/invert-binary-tree/discuss/62714/3-4-lines-Python