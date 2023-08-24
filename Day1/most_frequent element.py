def maximum_(arr):
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    mx=0
    most_frequent=None
    for element,value in d.items():
        if value > mx:
            mx=value
            most_frequent=element
    print(most_frequent)

list=[1,2,2,22,2,3,4,3,23,12,3]

maximum_(list)
    
    
