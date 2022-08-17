# Question
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Contraints: 
* 2 <= nums.length <= 104
* -109 <= nums[i] <= 109
* -109 <= target <= 109
* Only one valid answer exists.

# Understanding the Question
Input: A list of integers between 2 to 10^4 and an interger we want to add to
Output: A list of size 2 that contains that index that add up to the target (i.e the sum)

* We can have repeats ex/ [2, 2, 2]

# Brainstorm
* One solution is to have a nested for-loop and we would check if the values add up to the target. If they do, then return the indexes. Since we need two values, we need to check beforehand if they're the same index. However, this would take too long. 
* We can use a data structure to keep track of the values we've seen so far. If the data structure contains the value we seen that adds up to the target, then we returned those indices. We need to keep track of the value and the index (they're treated like a pair) so it would a dictionary would be good. If we seen the pair, return its index and the index we've seen. Otherwise, add it to the DTS. 

# Algorithm
1. Intialize a dictionary

2. Iterate through each value in the list:
    * Find the difference between the target and the current value.
    * If the difference is in the dictionary, return the current index and the index of difference
    * Otherwise, add the number you seen with the current value as the key and the index as the value 

# Write Your Code
```
def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {}
    
    for i in range(len(nums)):
        difference = target - nums[i]
        
        if difference in seen.keys():
            return [i, seen[difference]]
        else: 
            seen[nums[i]] = i
```

# Testing & Reflection 
## Test Cases
* List with two integers
* Typical Case
* List with the maximum length
* List with negative integers (including the minimum value)
* List that contains that maximum value

## Analysis
Time Complexity: O(n) -> worst case is that you have to iterate through the entire list
Space Complexity: O(n) -> worst case is that we have to store the entire list except one