def mergesort(A, p, r):
    if p<r:
        q = (p+r)//2
        mergesort(A, p, q)
        mergesort(A, q+1, r)
        merge(A, p, q, r)
        
    return A

def merge(A, p, q, r):
    temp = []
    i = 0
    j = 0
    t = 0
    
    while (p+i<=q) and (q+1+j<=r):
        if A[p+i]<A[q+1+j]:
            temp.append(A[p+i])
            i += 1
            t += 1
        else:
            temp.append(A[q+1+j])
            j += 1
            t += 1
    #sort if left list is not sorted 
    while p+i<=q:
        temp.append(A[p+i])
        i += 1
        t += 1
    #sort if right list is not sorted
    while q+1+j<=r:
        temp.append(A[q+1+j])
        j += 1
        t += 1
     #store the temp list into orginal list
    t = 0
    while p+t<=r:
        A[p+t] = temp[t]
        t += 1
        
    return A
