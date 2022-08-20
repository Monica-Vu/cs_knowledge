# Binary Search
An efficient search algorithm to find an element's position in a sorted array or list by repeatedly diving the search interval in life. 

**Time Complexity:** O(log n)

# Algorithm
1. Find approximately the middle of the array of list.
2. If the middle element is equal to the value we're looking for, return it (or its index).
3. however, if the current middle element is less than the value we're looking for, then we need to look in the upper half (right side of middle). Otherwise, we need to look for the lower half (left side of middle).
4. Repeat step 3 until the value is found or the interval is empty.

# Code
## Iterative Method
```
def binary_search_iterative(arr, target, low, high):
    while high >= low: 
        mid = low + (high - low)//2

        if arr[mid] == target:
            return "The element was found at position {}".format(mid)

        elif arr[mid] < target:
            low = mid + 1 

        else:
            high = mid - 1 
    
    return "The element was not found in the list."
```

## Recursive Method
```
def binary_search_recursive(arr, target, low, high): 
    if high >= low:
        mid = low + (high - low)//2

        if arr[mid] == target:
            return "The element was found at position {}".format(mid)
        
        elif arr[mid] < target: 
            return binary_search_recursive(arr, target, mid + 1, high)
        
        else: 
            return binary_search_recursive(arr, target, low, mid - 1)

    else:     
        return "The element was not found in the list."
```

# Test Cases
* Empty List
* List with One Item (has target)
* List with One Item (no target)
* List with Two Items (has target)
* List with Two Items (no target)
* List with Odd Number of Items & Greater Than Two (has target)
* List with Odd Number of Items & Greater Than Two (no target)
* List with Even Number of Items & Greater Than Two (has target)
* List with Even Number of Items & Greater Than Two (no target)
* Long list

# Resources 
https://www.geeksforgeeks.org/binary-search/

https://www.programiz.com/dsa/binary-search