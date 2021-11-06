# Problem
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Input: head = [1,2]
Output: [2,1]

Input: head = []
Output: []

**Constraints:**
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

# Questions, Clarification & Assumptions
**Possible Questions**
* Is the input only a number? 

**Assumptions**
* Single linked list as expected input and output type 

**Input:** A single linked list of 0 to 5000 numbers ranging from -5000 to 5000
**Output:** A single linked list of 0 to 5000 numbers ranging from -5000 to 5000 but reversed (so first element switches places with last element, second element switches plaecs with second last element)

**Possible Test Cases**
* Empty Linked List (Example 3)
* 1 Node
* 2 Nodes (Example 2)
* Normal Case (Example 1)
* Length of 1000 nodes
* Try different values

# Brainstorm
* In a Linked List, we often change pointers of `next` or `previous` (if applicable) when adding or deleting nodes 
* Maybe we can do the same idea for reversing
* This will be helpful to draw it out

# Algorithm
* Intialize a variable called `prev_node` to null
* Intialize a variable called `curr_node` to the head
* While the `curr_node` is not null:
    * set the `next_node` as current `curr_node` 's next 
    * set the `curr_node`'s next as `prev_node` 
    * set `prev_node` as `curr_node` 
    * set `curr_node` to `next_node` 

# Write Your Code
* As you go through your code, mention what need you plan to implement 
* Explain why you might be writing particular syntax 

```
def reverse_list(head):
    prev_node = None
    curr_node = head

    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node 
        prev_node = curr_node
        curr_node = next_node
    
    self.head = prev_node 

    return prev_node
```

# Testing & Reflection 
See [Possible Test Cases]

**Time complexity:** O(n) -> need to go through each node 
**Space Complexity:** O(1) -> only need to store pointer to three nodes at a time 

# Sources
https://leetcode.com/problems/reverse-linked-list/