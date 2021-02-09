#sort the given list and return the position of median
def sort_and_get_median(data, start, end):
    data[start:end+1] = sorted(data[start:end+1])
    return (start+end)//2
##################################################################
def choose_pivot(data, start, end):
    if end-start<5:
        return sort_and_get_median(data, start, end)
    
    #find the median and move that in front of list
    cur = start
    for i in range(start, end+1, 5):
        median_loc = sort_and_get_median(data, i, min(i+4, end))
        data[cur] , data[median_loc] = data[median_loc], data[cur]
        cur += 1
    
    #now the median elements are placed from 0 to cur
    return quickselect_pos(data, start, cur-1, (cur+start-1)//2)
##################################################################
#return pivot position's right location
def partition(data, start, end, pivot_pos):
    data[end], data[pivot_pos] = data[pivot_pos], data[end]
    standard = data[end]
    part_1 = start
    
    for part_3 in range(start, end+1):
        if data[part_3]<standard:
            temp = data[part_1]
            data[part_1] = data[part_3]
            data[part_3] = temp
            part_1 += 1
            
    temp = data[part_1]
    data[part_1] = data[end]
    data[end] = temp
    
    return part_1
###################################################################
#return selected position not value
def quickselect_pos(data, start, end, k):
    if start == end:
      return start
    
    pivot = choose_pivot(data, start, end)
    partition_ = partition(data, start, end, pivot)
    
    if partition_ == k:
        return partition_
    elif partition_ > k:
        return quickselect_pos(data, start, partition_-1, k)
    elif partition_ < k:
        return quickselect_pos(data, partition_+1, end, k)
##################################################################   
#return selected kth value of the list
def quickselect(data, start, end, k):
    if start == end:
        return data[start]
    
    pivot = choose_pivot(data, start, end)
    
    partition_ = partition(data, start, end, pivot)

    if partition_ == k:
        return data[partition_]
    elif partition_ > k:
        return quickselect(data, start, partition_-1, k)
    elif partition_ < k:
        return quickselect(data, partition_+1, end, k)
    
