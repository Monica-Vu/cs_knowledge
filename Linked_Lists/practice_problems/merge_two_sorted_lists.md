# Problem
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 
**Constraints:**
* The number of nodes in both lists is in the range [0, 50].
* -100 <= Node.val <= 100
* Both list1 and list2 are sorted in non-decreasing order.

# Brainstorm
Input: Wwo SLL linked list with integers in ascending order represented as l1 and l2
Output: One SLL formed from the two lists in ascending order 

* Since we know the list is sorted, we can just compare the head of the the two lists and see which one is smaller. If it's smaller, we set that as the next pointer.
* We don't need another SLL because we can just change the next pointers 
* We can use a dummy node to keep track of the head of the list and the current node will represent our last item

## Solution - Iterative Using a Dummy Node
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyNode = currNode = ListNode(0)
        
        while l1 and l2:
            if l1.val < l2.val: 
                currNode.next = l1
                l1 = l1.next
            else:
                currNode.next = l2
                l2 = l2.next
                
            currNode = currNode.next
        
        currNode.next = l1 or l2
        return dummyNode.next
```
# Test Cases
* Both are empty
* L1 is empty
* L2 is empty
* One node in L1 and L2 is empty 
* One node in L2 and L1 is empty 
* Two nodes in L1 and L2 is empty 
* Two nodes in L2 and L1 is empty 
* Typical Case 
* Big case

# Analysis
Time Complexity: O(n) -> need to iterate through entire items of l1 and l2
Space Complexity: O(1) -> Regardless of the size of the list, we only have to store one dummy node 

# Source
https://leetcode.com/problems/merge-two-sorted-lists/
https://leetcode.com/problems/merge-two-sorted-lists/discuss/9735/Python-solutions-(iteratively-recursively-iteratively-in-place).