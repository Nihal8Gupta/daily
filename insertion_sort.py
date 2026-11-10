def insertion_sort(nums:list):
    length = len(nums)
    for i in range(1,length):
        j = i - 1
        key = nums[i]
        while j >=0 and nums[j] > key:
            nums [j + 1] = nums[j]
            j -= 1 
        nums[j + 1] = key
    return nums


print(insertion_sort([3,1,6,8,0,2,7]))