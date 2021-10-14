# Problem 
Given the root of a binary tree, invert the tree, and return its root.

## Constraints:
* The number of nodes in the tree is in the range [0, 100].
* -100 <= Node.val <= 100

# Test Cases
* Empty Tree
* Tree only only one node
* Tree has three nodes and the leaves have the same value (tree is symmetrical)
* Tree is asymmetrical 
* Tree is symmetrical but contains different values
* Left-skewed Tree
* Right-skewed Tree
* A tree with lots of nodes (performance)

# Asymptotic Analysis 
Time Complexity: O(n) --> need to visit every node and flip it. 

# Sources
https://leetcode.com/problems/invert-binary-tree/
https://leetcode.com/problems/invert-binary-tree/discuss/62714/3-4-lines-Python