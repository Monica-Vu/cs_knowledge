def containsDuplicateSol1(nums: List[int]) -> bool:
    unique_elements = set()
    
    for item in nums:
        if item in unique_elements:
            return True
        else:
            unique_elements.add(item)
    
    return False

def containsDuplicateSol2(nums: List[int]) -> bool:
    return len(nums) != len(set(nums))