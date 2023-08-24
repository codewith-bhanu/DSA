def minimum_(arr):
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    min=float("inf")
    min_frequent=None
    for element,value in d.items():
        if value<min:
            min=value
            min_frequent=element
    print(min_frequent)

list=[1,1,2,2,22,22,2,3,12,3,23,12,3]

minimum_(list)
    
    
