# Problem
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

You must write an algorithm that runs in O(n) time and without using the division operation.
 
## Examples 
### Example 1
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

### Example 2
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 
## Constraints
* 2 <= nums.length <= 105
* -30 <= nums[i] <= 30
* The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

## Follow up
Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

# Brainstorm
* One possible idea is to create a double for-loop. We let the outer loop as the element we're skipping and the inner for-loop to perform the multiplication 
* Notice that if we're excluding the first element, we're only multiplying items on its right. If we're excluding the last element, we're only multiplying items to the left. If we pick an element in the middle, we just multiply the items on the left and on the right of it. So let's try to create an algorithm based off this.  
* We can use an additional list to store the left product and then multiply that to get the right product

# Algorithm
1. With the exception of the first item and the last item, we can find the product without self by multiplying the product of all elements in the left-hand side by the product of all elements in the right-hand side of the element 
2. For the first element, we find the product of just its left-hand side.
3. For the last element, we find the product of just its right-hand side.

**Notes**

**Test Cases:** 
* Two elements in `nums` 
* Normal-length list without 0
* Normal-length list with 0 
* Ensure you have cases where -30 and 30 are included

# Sources
https://leetcode.com/problems/product-of-array-except-self/discuss/210147/Java-Python-Thinking-Process-with-Followup