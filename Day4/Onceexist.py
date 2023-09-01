def once_num(arr):
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1

    Once=None

    for i, j in d.items():
        if j==1:
            Once=i

    print(Once)

l=[2,2,3,4,5,3,4,5,1]

once_num(l)
            
