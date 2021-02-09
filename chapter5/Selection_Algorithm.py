def partition(A, p, r):
    standard = A[r]
    part_1 = p
    
    for part_3 in range(p, r):
        if A[part_3] <= standard:
            temp = A[part_1]
            A[part_1] = A[part_3]
            A[part_3] = temp
            part_1 += 1
    
    temp = A[r]
    A[r] = A[part_1]
    A[part_1] = temp
    
    return part_1

#select ith element in sorted array A[p,,,r]
def select(A, p, r, i):
    #if there's only one element in array A, then return that element
    if p == r:
        return A[p]
    
    q = partition(A, p, r)
    
    #k : kth element in sorted array A
    k = q-p+1
    
    #if k>i implement the function again until k=i
    if k > i:
        return select(A, p, q-1, i)
    
    #if k=i then return that element
    elif i == k:
        return A[q]
    
    #if k<i then implement the function again start with q+1,
    #we already found kth element so find (i-k)th element 
    else:
        return select(A, q+1, r, i-k)
