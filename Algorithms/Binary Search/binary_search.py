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

def main(): 
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    low = 0 
    high = len(arr) - 1
    
    print(binary_search_iterative(arr, 7, low, high))
    print(binary_search_iterative(arr, 12, low, high))
    print(binary_search_recursive(arr, 7, low, high))
    print(binary_search_recursive(arr, 12, low, high))

main()