def two_sum(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:

                return [i,j]

l=[2,5,3,7]
target=9


print(two_sum(l,target))
