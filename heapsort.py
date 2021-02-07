def buildHeap(A, n):
    #build heap from bottom 
    for i in range(n//2, -1, -1):
        heapify(A, i, n)
    
    return A

def heapify(A, k, n):
    left = 2*k
    right = 2*k+1
    #check the right node
    if right < n:
        if A[left] <= A[right]:
            smaller = left
        else:
            smaller = right
    
    #check the left node if there's no right node
    elif left < n:
        smaller = left
        
    #if there's no node, then k is leaf node->end the function
    else: 
        return A
    
    #if parent is smaller than left or right node-> swap and heapify again
    if A[k] > A[smaller]:
        temp = A[k]
        A[k] = A[smaller]
        A[smaller] = temp
        heapify(A, smaller, n)
        

def heapSort(A, n):
    #At first, make a list as a heap
    buildHeap(A, len(A))
    list_len = len(A)
    for i in range(len(A)-1, 0, -1):
        #exchange between current element and top node
        temp = A[i]
        A[i] = A[0]
        A[0] = temp
        #decrease the list size
        list_len -= 1
        
        #compare between changed current element and child nodes 
        #if current node is greater than child nodes, than heapify
        #and make list as a heap again
        heapify(A, 0, list_len)
    
    for i in range(len(A)//2):
        temp = A[i]
        A[i] = A[(len(A)-1)-i]
        A[(len(A)-1)-i] = temp
    
    return A
