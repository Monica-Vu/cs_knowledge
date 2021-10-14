# Assumptions
* The following code exists:
## Graph
```
class Graph:
    def __init__(key):
        self.root = key
```

## Node
Each node in the BST has a `key` and points to its left and right child. 

```
class Node:
    def ___init___(self, key):
        self.key = key
        self.left = None
        self.right = None
```

# Pre-order 
## Algorithm
1. Visit the node (root).
2. Visit the left subtree.
3. Visit the right subtree.

## Code
```
def preorder(root):
    if root:
        print(root)
        preorder(root.left)
        preorder(root.right)
```

## Use Case(s)
* Build BST

# In-order
## Algorithm
1. Visit the left subtree.
2. Visit the node (root).
3. Visit the right subtree.

## Code 
```
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key)
        inorder(root.right)

```

## Use Case(s)
* Find sorted output of a tree.

# Post-order 
## Algorithm
1. Visit the left subtree.
2. Visit the right subtree.
3. Visit the node.

## Code 
```
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root)

```

## Use Case(s)
* Build BST

## How to Calculate Time and Space Complexity of BST Algorithms
You can determine time complexity by determining how many nodes (n) we have to visit along with the amount it takes to perform in each node (k), which would equal to O(n * k) of the worst case scenario. 



# Source(s)
https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/

https://youtu.be/YbZpsloJ9YQ