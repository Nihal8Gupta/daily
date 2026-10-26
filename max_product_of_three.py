class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
    
s = Solution()
print(s.maximumProduct([-10, -10, 5, 2]))  # Output: 500