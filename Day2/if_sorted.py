def is_sorted(arr):
    # Check for ascending order
    is_ascending = all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
    
    # Check for descending order
    is_descending = all(arr[i] >= arr[i+1] for i in range(len(arr)-1))
    
    # Return True if either ascending or descending
    return is_ascending or is_descending

# Test cases
array1 = [1, 2, 3, 4, 5]
array2 = [5, 4, 3, 2, 1]
array3 = [1, 3, 2, 4, 5]

print(is_sorted(array1))  
print(is_sorted(array2))  
print(is_sorted(array3))  
