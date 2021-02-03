def SelectionSort(x):
    last = len(x)-1
    for n in range(last, 1, -1):
        max_ = x[n]
        loc = n
        for j in range(n):
            if max_<x[j]:
                max_ = x[j]
                loc = j
        temp = x[n]
        x[n] = max_
        x[loc] = temp
    return x

