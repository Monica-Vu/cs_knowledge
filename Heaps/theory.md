# Binary Heaps
A data structure to a binary tree with the following additional properties: 
(1) It must be a complete binary tree: all levels are completed filled EXCEPT maybe the last one. The last-level must ensured the left-most nodes are filled FIRST.

(2) The children of the root must either be greater or equal (minimum heap) or less than or equal to its children (maximum heap)

* The root is always the minimum or maximum (only thing that is guranteed) 
* There can be be duplicates
* Can be represented as a linked list or a tree (preferred method)
    * If represented as an array, the left child and the right children can respectively represented with positions 2i + 1 and 2i + 2
    * The parent can be determined by subtracting 1, dividing by two, and rounding down (i.e floor operation)

## Minimum Heap Representation
```
       5
     /   \
   12    20
  /  \   
 25  13 
```

## Maximum Heap Representation
```
       58
     /    \
   120     200
  /  \   
 250  130 
```

# Uses
* Top or lowest k (or items) for minimum heap and maximum respectively

# Implementation
## Adding a Node
* Add the item to the left-most available spot of the lowest level
* If we find the item is larger or smaller than the root, then we swap the places of the two nodes

## Deleting the Root
* Delete the root
* Set the right-most node of the lowest level as the root (and remove it)
* If the heap-order property is violated, "bubble down" the current root node until all parent nodes are greater/less than or equal to their child nodes

# Source(s)
https://medium.com/basecs/learning-to-love-heaps-cef2b273a238