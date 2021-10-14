def product_except_self(nums):
    nums_len =  len(nums)          
    result = [1] * nums_len        
    
    """
    Get the left product for each element. 
    To do this, we know that the previous element in the result list is the product of the previous element. 
    Thus, the element to the right just has to multiply its current value to get the product. 
    """
    for i in range(1, nums_len):    
        result[i] = result[i - 1] * nums[i - 1]
    
    """
    The last element doesn't have any element next to it (hence why we multiply by 1).
    To get the product of right, we continue multiply right_product as we iterate backwards.
    """
    right_product = 1   
    for i in range(nums_len - 1, -1, -1):
        result[i] *= right_product
        right_product = right_product * nums[i]
    
    return result

print(product_except_self([2, 3])) # expecting: [3, 2]
print(product_except_self([1, 2, 3, 4])) # expecting: [24, 12, 8, 6]