def frq(arr):
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    print(d)

list=[1,2,2,22,2,3,4,3,23,12,3]

frq(list)
