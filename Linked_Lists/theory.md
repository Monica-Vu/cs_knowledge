# About
A data structure that represents sequential data where each data is stored in a node. It typically has a head and sometimes a tail. Depending on the type, it has either a pointer to the next node (singly linked list) or pointers to the next node and the previous node. 

# Advantages
* Insertion and deletion of a node given its location is O(1) whereas lists will have to be shifted but extra memory is required to store the node and the data

# General Tips 
* It might be useful to have a dummy node so operations never have to be done on the head or tail and null-checs are not required 
* When possible, use a doubly linked list (but something to clarify for interviews)
* Borrow ideas from the "reverse a linked list" problem to reduce storage 
* To partition a linked list, create two seperate linked list and join them together
* Use Two Pointers and Fast & Slow Pointers ex/ getting kth last node, detect cycles, get middle node

# Common Algorithms to Know
## Count Number of Nodes
```
def count_num_nodes(head):
    count = 0
    curr_node = head

    while curr_node:
        count += 1
        curr_node = curr_node.next 
    
    return count

```

## Reverse Linked List In-Place

## Find Middle Node 

## Merge Two Linked List 

# Common Corner Cases 
* Single node
* Two nodes
* Cycled Linked List (typical not the case but clarify)