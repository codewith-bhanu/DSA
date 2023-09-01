def find_missing(arr):

    n=len(arr)
    sum=(n+1)*(n+2)//2
    total=0
    for i in range(n):
        total+=arr[i]

    miss=sum-total
    return miss

l=[1,2,3,4,6]

print(find_missing(l))
