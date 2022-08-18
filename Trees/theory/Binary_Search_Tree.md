# Binary Search Tree
**Reminder:** A Binary Tree has at most two children. 

Nodes in a Binary Search Tree (BST) have an optional attribute called "key" (equivalent to a value in a given node in Linked List). 

## Properties
* The key of the left subtree is less than the parent.  
* the key of the right subtree is greater than the parent
* No duplicate nodes

## Advantages
* Ordering allows operation like search or finding the minimum or maximum can be performed more quickly

# Sample Representation 
```
       27
     /    \
   14     30
  /  \   /  \
 10  17 28  39  
      \ 
       20
```
# Code Representation (Python)
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

# Basic Operations
## Search
### Algorithm
* Compare the key to the root's key. If it's the same or the root's key is null, end the search. 
* Otherwise checking for the following:
    * If the key is greater than the root's key, recurse with the right subtree. 
    * If the key is less than the root's key, recurse with the left subtree

#### Example 
Let's say we want to find 20 in the following BST:
```
       27
     /    \
   14     30
  /  \   /  \
 10  17 28  39  
      \ 
       20
```

1. We start at `27` and see that the `27` (root.key) is less than `20`. So we visit the left subtree.
2. We're now at `14` (new root). Is `20` == `14`? NO! we see that `20` (key) > `14` (root.key). So we visit the right subtree.
3. We're now at `17` (new root). Is `20` == `17`? NO! `20` (key) > `17` (root.key) so, we go to the right subtree.
4. We're now at `20`. `20` == `20`? Yes! We found the node.

### Code 
```
def search(self, root, key):
    # base case: root is null (returns false value) or has the as key being searched for
    if root is None or root.key == key:
        return root
    
    # the key is greater than the root/parent, go to the right subtree
    elif root.key < key:
        return self.search(root.right, key)
    
    # otherwise, search for the left subtree 
    else:
        return self.search(root.left, key)

```
**Note(s)**:
* You can put this under the `Graph` class or as a seperate function

### Asymptotic Analysis 
**Time Complexity:** O(h) -- worst case is when we're searching for a leaf node (so we reach the end of the tree's height)
**Space Complexity:** O(1) -- we don't use any data structures in this algorithm regardless of the size of the BST.

## Insertion
### Algorithm
* Compare the key to the root's key. If the root is empty (i.e we reached a leaf node), we insert it here.
* Otherwise checking for the following:
    * If the key is greater than the root's key, recurse with the right subtree. 
    * If the key is less than the root's key, recurse with the left subtree

#### Example 
Let's say we want to insert 11 in the following BST:
```
       27
     /    \
   14     30
  /  \   /  \
 10  17 28  39  
      \ 
       20
```
1. The root is not empty. `11` is less than 27 so we recurse to the left subtree.
2. The root of this left subtree is not empty. So we check if `11` is greater or less than `14` (current root key).  

### Code
```
def search(self, root, key):
    # base case: root is null or has the as key being searched for
    if root is None or root.key == key:
        return root
    
    # the key is greater than the root/parent, go to the right subtree
    elif root.key < key:
        return self.search(root.right, key)
    
    # otherwise, search for the left subtree 
    else:
        return self.search(root.left, key)

```
**Note(s)**:
* You can put this under the `Graph` class or as a seperate function

### Asymptotic Analysis 
**Time Complexity:** O(h) -- we have to go travel from the root to the deepest node. This should cost O(log n) but can become O(n) if the tree becomes skewed.
**Space Complexity:** O(n)

## Deletion

### Algorithms
#### Deleted Node is a Leaf
* Use the search algorithm to find the node to delete
* Once node is found, delete it

**Example:**
Let's say we want to delete `20` in the following BST:

Before:
```
       27
     /    \
   14     30
  /  \   /  \
 10  17 28  39  
      \ 
       20
```

After:
```
       27
     /    \
   14     30
  /  \   /  \
 10  17 28  39  
```
1. Use the `search` algorithm to find `20` 
2. Delete `20` node

#### Deleted Node has a Child
* Use the search algorithm to find the node to delete
* Copy the deleted node's child and set that as the deleted's node parent

**Example:**
Let's say we want to delete `17` in the following BST:

Before:
```
       27
     /    \
   14     30
  /  \   /  \
 10  17 28  39  
      \ 
       20
```

After:
```
       27
     /    \
   14     30
  /  \   /  \
 10  20 28  39  
```


1. Use the `search` algorithm to find `17` 
2. Set the parent of `17`'s child as `20`

#### Deleted Node has a Child
* Use the search algorithm to find the node to delete
* Find the inorder successor (deleted node's right leftmost child)

**Example:**
Let's say we want to delete `14` in the following BST:

Before:
```
       27
     /    \
   14     30
  /  \   /  \
 10  17 28  39  
      \ 
       20
```

After:
```
       27
     /    \
   17     30
  /  \   /  \
 10  20 28  39  
```

1. Use the `search` algorithm to find `14` 
2. Find the inorder successor of 14 (i.e smallest child in the right value), which is 17.
3. Set the successor's place as `14` 


### Code
```
def min_node_value(node):
    curr = node

    while curr.left is not None:
        curr = curr.left 
    return curr

def delete_node(root, key):
    # base case
    if root is None:
        return root

    # key must be in left subtree
    if key < root.key: 
        root.left = delete_node(root.left, key)
    
    # key must be in right subtree
    elif (key > root.key):
        root.right = delete_node(root.right, key)
    
    # found node to be deleted 
    else:
        # deleted node is leaf node
        if root.left is None and root.right is None:
            return None 

        # deleted node has one child 
        if root.left is None: 
            temp = root.right
            root = None
            return temp 
        elif root.right is None:
            temp = root.left
            root = None
            return temp 
        
        # node w/ two different children -- find inorder successor (smallest value in the right tree)
        temp = min_node_val(root.right)

        # copy contents of smallest tree
        root.key = temp.key 

        # delete inorder successor
        root.right = delete_node(root.right, temp.key)
    
    return root

```

#### More Efficient Deletion for Node with Two Children
```
successor_parent = root
successor = root.right

while successor.left != None:
    successor_parent = successor
    successor = successor.right

"""
Delete successor.
The successor is always the left child of its parent so we can safely make successor's right child as left of its parent. Otherwise, we set it as it is. 
"""
if successor_parent != root:
    successor_parent.left = successor.right
else:
    successor_parent.right = successor.right

# copy 
root.key = successor.key
```

### Asymptotic Analysis 
**Time Complexity:** O(h) -- we have to go travel from the root to the deepest node. This should cost O(log n) but can become O(n) if the tree becomes skewed.
**Space Complexity:** O(h) -- worst case is we store the depth of the tree in the stack

# Source(s)
https://www.tutorialspoint.com/data_structures_algorithms/binary_search_tree.htm

https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/

# Review Questions
1. What is a binary search tree and its main key properties?