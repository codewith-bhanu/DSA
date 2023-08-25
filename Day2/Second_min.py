def second_min(arr):
    min=arr[0]
    second_min=float("inf")
    for i in range(len(arr)):
        if(arr[i]<min):
            second_min=min
            min=arr[i]
        elif(arr[i]>min and arr[i]<=second_min):
            second_min=arr[i]

    print(second_min)

l=[1,2,3,4,5,5,6]

second_min(l)


