def four_sum(arr,target):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    
                    if(arr[i]+arr[j]+arr[k]+arr[l]==target):
                        
                        return [i,j,k,l]

l=[2,3,4,5,6,2,3]
print(four_sum(l,10))
