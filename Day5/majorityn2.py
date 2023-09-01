
def majority_element(arr):
    m=dict()
    for i in arr:
        if i in m:
            m[i]+=1
        else:
            m[i]=1
    majority=None
    for i,j in m.items():
        if j>(len(arr)/2):
            majority=i
    return majority

    


l=[2, 2, 1, 1, 1, 2, 2]

print(majority_element(l))
            
