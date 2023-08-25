def sorted(arr):
    n=len(arr)
    for i in range(1,n):
        if(arr[i-1]<arr[i]):
            return True
        else:
            return False
    return True

def check_sorted(arr):
    if sorted(arr)== True:
        print("Array is sorted")
    elif sorted(arr)== False:
        print("Array is not sorted")


l=[3,1,2,3,4,5,6]
check_sorted(l)
