def is_increasing(arr):
	if len(arr) <= 1:
			return True 

	for i in range(1, len(arr)):
		if arr[i - 1] >= arr[i]:
				return False 
		continue 

	return True

print(is_increasing([]))   # True 
print(is_increasing([1]))   # True 
print(is_increasing([1, 2, 6, 10]))   # True 
print(is_increasing([1, 4, 2, 10]))   # False 
print(is_increasing([1, 4, 4, 6, 10]))  # False 
print(is_increasing([1, 4, 6, 4, 10]))  # False 
print(is_increasing([1, 4.1, 6, 4.2, 10]))  # False 