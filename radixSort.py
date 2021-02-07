def extract_num(num, i):
    divider = 10**(i)
    first = num%divider
    ans = first//(divider/10)
    
    return int(ans)


def radixSort(A, n, k):
    temp = A
    for i in range(1, k+1, 1):
        #make a room for each digits(using dictionary)
        dic = {}
        for j in range(10):
            dic[j] = []
        
        #extract the digits from each list elements and put the element is 
        #right dictionary
        for j in range(n):
            last_num = extract_num(temp[j], i)
            dic[last_num].append(temp[j])
        
        #rearrange the dic as one list
        temp = []
        for j in range(10):
            temp += dic[j]
        
    return temp
