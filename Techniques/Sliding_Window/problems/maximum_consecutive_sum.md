# Problem 
Give a list of integers of size n. Calculate the maximum of 'k' consecutive elements. 

Example 1:
Input: l = [100, 200, 300, 400], k = 2
Output: 700 because 300 + 400 = 700

Example2: 
Input: l = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4
Output: 39 because 4 + 2 + 10 + 23 = 39

Example 3:
Input: l = [2, 3], k = 3
Output: Invalid because the length of the list is less than `k`

# Questions and Clarifications
* Is the input always invalid (i.e `l` is always a list of integers and `k` is always an integer)?
* What are the minimum and maximum length and values of the string? What about k? 
* Is there any constraints or restrictions in how I solve the problem?

# Solutions
## Naive Approach via Brute Force
* Starting with the index, sum till k-th element. Repeat this for all groups of k.
* Uses nested loop

### Code
```
def find_max_sum_brute_force(l, k): 
    max_sum = float('-inf')
    length = len(l)

    for i in range(length - k + 1): 
        curr_sum = 0
        for j in range(k):
            curr_sum += l[i + j]
        
        max_sum = max(curr_sum, max_sum)
    
    return max_sum
```

### Analysis
Time Complexity: O(k * n) -> two nested loops 
Space Complexity: O(1) -> always just store the length, max_sum, and curr_sum

## Sliding Window Technique
* Find the sum of the first k elements (this is our window)
* Subtract the element of the first element in the window
* Add the next element to the last element in the window
* Repeat until we reach the end of the list

### Code
```
def find_max_sum_sliding_window(l, k):
    length = len(l)

    if length < k:
        print("Invalid")
        return -1 
    
    window_sum = sum(l[:k])
    max_sum = window_sum

    for i in range(length - k):
        window_sum = window_sum - l[i] + l[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum
```

### Analysis
Time Complexity: O(n)
Space Complexity: O(1) -> we're always just storing three integers 

# Test Cases
* Possibly a different type of input expected for `k` or `l`
* Empty list
* List where length is less than k
* List where length == k
* List where length > k
* List with maximum length

# Resources
https://www.geeksforgeeks.org/window-sliding-technique/