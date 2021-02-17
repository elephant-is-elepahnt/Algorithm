def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)
        
    return A


def partition(A, p, r):
    #choose last element of selected list as a standard element x
    #three parts
    #parts 1 : i -> less than standard element x
    #part 2  -> larger than standard element x
    #part 3 : j -> not selected yet
    x = A[r]
    #make part 1
    i = p
    
    #make part 2, j stands for part 3 that are not selected yet
    for j in range(p, r):
        #if A[j] is less than standard element make a room for part 1 
        #and swap with part 3
        if A[j] <= x:
            temp = A[i]
            A[i] = A[j]
            A[j] = temp
            i += 1
            
    #move standard element between part 1 and part 2
    #we already make a room in last for statement so we don't have to 
    #i+1 at this time
    temp = A[i]
    A[i] = x
    A[r] = temp
    
    return i
