# Binary Tree
A tree that contains at most two children (left and right child)

## Components
* Data
* Pointer to Left Child
* Pointer to Right Child

## Types
* **Full**: a tree where every node has either two children or no children
* **Perfect**: All nodes have exactly two children and all leaf nodes are at the same level 
* **Complete**: 
    * every node has two children or no children
    * Every level is completed filled
    * All elements must lean towards the left
    * The last leaf element might not have a right sibling 

```
       27
     /    \
   14     30
  /  \   /  
 10  17 28  
```

* **Degenerated or Pathological**: A tree where each node has a single child 
```
       1
     /   
   2    
    \    
     3   
      \    
       4   
```

* **Skewed**: A tree where there are only right nodes or left nodes
``` 
   2                     1
    \                   /
     3                 2 
      \               /
       4             3
``` 

* **Balanced**: A tree where the height difference between is the left subtree and right subtree is 1 or 0.

# Common Terminology
**Ancestor**

**Descendant**

**Child** 

**Leaf** 

**Height** 

# Resources
https://www.programiz.com/dsa/binary-tree