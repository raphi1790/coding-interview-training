
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    
    middle = len(arr)//2
    lhs = arr[0:middle]
    rhs = arr[middle:]

    sorted_lhs = merge_sort(lhs)
    sorted_rhs = merge_sort(rhs)
    
    return _combine(sorted_lhs, sorted_rhs)   


def _combine(lhs, rhs):
    if lhs is None:
        return rhs
    if rhs is None:
        return lhs

    lhs_idx = 0
    rhs_idx = 0
    sorted_list = []
    while lhs_idx < len(lhs) and rhs_idx < len(rhs):
        left_number = lhs[lhs_idx]
        right_number = rhs[rhs_idx]
        
        if left_number < right_number:
            sorted_list.append(left_number)
            lhs_idx += 1
        else:
            sorted_list.append(right_number)
            rhs_idx += 1

    sorted_list += lhs[lhs_idx:]
    sorted_list += rhs[rhs_idx:]
    
    return sorted_list



if __name__ == "__main__":
    sorted = merge_sort([2,1,7,4,3])
    print(sorted)