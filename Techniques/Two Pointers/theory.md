# Two Pointers
* You use two pointers to reduce the amount of times you may need to iterate on a linear data structure 
* Often used with sliding window

## Variations 
* Fast and Slow Pointer
* Pointers Moving towards each other to eventually meet

## Application
* Generally used to find pairs in sorted array

## Steps
* Intialize pointers ex/ same place, extreme ends
* Decide how pointers will move to get so the solution ex/ same direction, opposite direction and the increments they will move
* Identify condition when we stop ex/ when we reach the end, when the pointers pass each other, when pointers each the same place 

# Example Problems
* Remove Duplicates From a Sorted List
* Reversing a List 
* Order an Element with Squares of Numbers
* Does Linked List have a Cycle?
* Find the longest substring without repeating characters

```
def reverse(s):
    start = 0
    end = len(s) - 1

    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    
    return s

```

# Resources
https://leetcode.com/articles/two-pointer-technique/
https://towardsdatascience.com/two-pointer-approach-python-code-f3986b602640