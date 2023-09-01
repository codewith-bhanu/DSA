
def majority_element(arr):
    l=[]
    m=dict()
    for i in arr:
        if i in m:
            m[i]+=1
        else:
            m[i]=1
    
    for i,j in m.items():
        if j>(len(arr)/3):
            l.append(i)

    return l

    


l=[2, 2, 1, 1, 1, 2, 2]

print(majority_element(l))
            
