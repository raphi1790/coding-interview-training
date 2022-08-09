def can_partition_recursive(nums, current_idx, remaining_sum, subset):
    if current_idx == len(nums):
        return []
    
    if remaining_sum == 0:
        return subset

    v1 = can_partition_recursive(nums, current_idx+1, remaining_sum -nums[current_idx], subset + [nums[current_idx]])
    v2 = can_partition_recursive(nums, current_idx+1, remaining_sum, subset)

    return v1 or v2



def can_partition(nums, sum):
    subset = can_partition_recursive(nums,0,sum,[])
    return subset


if __name__ == "__main__":
    print(can_partition([1,2,3,4,7],6))