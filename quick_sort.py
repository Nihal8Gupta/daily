def quick(nums:list):
    if len(nums) <= 1:
        return nums

    pivot = nums[len(nums)//2]
    left = [ x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot] # duplicates
    right = [ x for x in nums if x > pivot]
    return quick(left) + middle + quick(right)

print(quick([3,1,1,6,8,3,0,2,7]))