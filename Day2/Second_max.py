def second_max(arr):
    max=arr[0]
    second_maxi=float("-inf")
    for i in range(len(arr)):
        if(arr[i]>max):
            second_maxi=max
            max=arr[i]
        elif(arr[i]<max and arr[i]>=second_maxi):
            second_maxi=arr[i]

    print(second_maxi)

l=[1,2,3,4,5,5,6]

second_max(l)


