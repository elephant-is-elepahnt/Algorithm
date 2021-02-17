def insertionSort(A, n):
    for i in range(1, n, 1):
        choosen = A[i]
        #A[0...i-1] already sorted
        loc = i-1
        while loc>=0 and choosen<A[loc]:
            temp = A[loc]
            A[loc] = choosen
            A[loc + 1] = temp
            loc -= 1
            
    return A
        
