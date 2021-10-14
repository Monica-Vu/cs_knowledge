"""
BRAINSTORM: 
- When we iterate through the list, we can decide to add the item to the list or not
- As we iterate through the list, we may find smaller elements -- this might allow us to extend the potential longest increasing subsequence
so we can replace it. 
- For the smallest number we encounter so far, we should make a new list and append the increasing values
- We'll have active lists with different lengths and eliminate lists EXCEPT the one with the smallest tail value 

ALGORITHM: 
ITERATE THROUGH THE LIST -- A:
1. If A[i] is smallest among all end candidates of the active list, we will create a new list of length 1.
2. If A[i] is the largest among all end candidates of active lists, we will clone the largest active list and extend it by A[i].
3. If A[i] is a value between the smallest and largest found so far, we will find a list with the largest end element than is smaller than A[i] and clone it.
Discard all other lists of the same length as the list that gets modified.

SOURCE(S):
https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
"""

def binary_search(array, left, right, key):
    while (right - left > 1):
        middle = left + (right - 1) // 2
        if array[middle] >= key:
            right = middle 
        else:
            left = middle 
    
    return right 

def LIS(A):
    length_A = len(A) 
    # this table represents the different "arrays" we holding 
    table = [0] * (length_A + 1)
    # max_length points to an empty slot
    max_length = 0

    table[0] = A[0]
    max_length = 1

    for i in range(1, length_A):
        if A[i] < table[0]: 
            table[0] = A[i]
        
        elif A[i] > table[max_length - 1]: 
            table[max_length] = A[i]
            max_length += 1
        
        else: 
            table[binary_search(A, -1, max_length - 1, A[i])] = A[i]
        
    return max_length

A = [ 2, 5, 3, 7, 11, 8, 10, 13, 6 ]
print(LIS(A))