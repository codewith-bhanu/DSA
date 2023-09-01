def three_sum(arr,target):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if(arr[i]+arr[j]+arr[k]==target):
                    return [i,j,k]

l=[2,3,4,5,6,3]
print(three_sum(l,10))
