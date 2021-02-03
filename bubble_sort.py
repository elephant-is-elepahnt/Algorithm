def bubblesort(x, n):
    for last in range(n, 1, -1):
        changed = False
        for i in range(0, last-1, 1):
            if x[i]>x[i+1]:
                temp = x[i+1]
                x[i+1] = x[i]
                x[i] = temp
                changed = True
        if changed == False:
            return x
    return x
