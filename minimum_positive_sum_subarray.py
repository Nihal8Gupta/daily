def minimumSumSubarray(nums: list, l: int, r: int) -> int:
    max_sum = []
    for length in range(l, r + 1):
        for i in range(len(nums) - length + 1):

            temp = sum(nums[i:i + length])

            if temp > 0:
                max_sum.append(temp)

    return -1 if len(max_sum) == 0 else min(max_sum)

print(minimumSumSubarray([1, 2, 3, -4, 5], 2, 3))  # Output: 1