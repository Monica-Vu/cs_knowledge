# Problem
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. **Note that pos is not passed as a parameter.**

Return true if there is a cycle in the linked list. Otherwise, return false.

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

**Constraints:**
* The number of the nodes in the list is in the range [0, 104].
* -105 <= Node.val <= 105
* pos is -1 or a valid index in the linked-list.

# Questions, Clarification & Assumptions
**Possible Questions**
* Is the input only a number? 
* Does -1 means that there's no linked list?

**Assumptions**
* Single linked list as expected input and output type 

**Input:** A single linked list of 0 to 104 numbers ranging from -105 to 105
**Output:** A boolean to indicate if there's a cycle 

**Possible Test Cases**
* Empty Linked List (No cycle)
* 1 Node (No cycle)
* 2 Nodes (No cycle)
* 2 Nodes (Cycle)
* Normal Case with Cycle (Example 1)
* Normal Case with no Cycle (Example 1)
* Length of 104 nodes with Cycle
* Length of 104 nodes with no Cycle
* Try different values from expected (since we're only looking for a node)

# Brainstorm
* If we have two pointers, the start and end will meet at some point 

# Algorithm
* Intialize two pointers at the start
* Set one pointer (fast) to be twice as fast as the second one
* Once they equal each other, it means there's a cycle
* Otherwise, they will hit the end 

# Write Your Code
* As you go through your code, mention what need you plan to implement 
* Explain why you might be writing particular syntax 

```
def linked_list_cycle(head):
    slow = fast = head

    while fast and fast.next: 
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return True
    return False 
```

# Testing & Reflection 
* See `Possible Test Cases`

**Time Complexity:** O(n) --> only need to iterate through the linked list
**Space Complexity:**  O(1) --> only two pointers stored regardless of size 

# Sources
https://leetcode.com/problems/reverse-linked-list/