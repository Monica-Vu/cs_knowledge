# brute force solution
def find_max_sum_brute_force(l, k): 
    length = len(l)

    if length < k:
        print("Invalid")
        return -1 

    max_sum = float('-inf')

    for i in range(length - k + 1): 
        curr_sum = 0
        for j in range(k):
            curr_sum += l[i + j]
        
        max_sum = max(curr_sum, max_sum)
    
    return max_sum

# sliding window 
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


# Main Code
l = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
print(find_max_sum_brute_force(l, k))
print(find_max_sum_sliding_window(l, k))