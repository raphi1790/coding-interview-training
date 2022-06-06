# time O(nlog(n))
# space 

def partition(nums, left_index, right_index):
    pivot = nums[right_index]
    pointer = left_index # will be the final position of the pivot. until then, it indicates the index which is just bigger than the pivot.

    for i in range(left_index, right_index):
        if nums[i] <= pivot:
            # on the right side of the pivot
            # swap current position with the index indicating the position of the 
            nums[i], nums[pointer] = nums[pointer], nums[i]
            pointer += 1
    
    # bring pivot to correct index, which will be pointer
    nums[pointer], nums[right_index] = nums[right_index], nums[pointer]
    # return correct index of pivot
    return pointer 

def quick_sort(nums,left_index, right_index):
    
    if len(nums) == 1:
        return nums
    
    if left_index < right_index:
        pointer = partition(nums, left_index, right_index)
        quick_sort(nums, left_index, pointer-1)
        quick_sort(nums, pointer+1, right_index) 

    return nums



def partition_in_place(nums, left_index, right_index):
    i = left_index +1
    j = right_index
    pivot = nums[left_index]
    
    while i<=j:
        if nums[i]> pivot and nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1
        elif nums[i]<=pivot:
            i+=1
        elif nums[j] >= pivot:
            j-=1
        else:
            i+=1
            j-=1
    nums[left_index], nums[j] = nums[j], nums[left_index]
    return j

def quick_sort_in_place(nums,left_index, right_index):
    
    if right_index- left_index <1:
        return 
    
    if left_index < right_index:
        pointer = partition_in_place(nums, left_index, right_index)
        quick_sort_in_place(nums, left_index, pointer-1)
        quick_sort_in_place(nums, pointer+1, right_index) 

    return nums


if __name__ == "__main__":
    nums = [2,1,7,4,3]
    sorted_nums=quick_sort_in_place(nums, 0, len(nums)-1)
    print(sorted_nums)
