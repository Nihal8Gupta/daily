class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        answer = [1] * length
        prefix = 1
        suffix = 1
        print('nums',nums)
        for i in range(length):
            answer[i] = prefix
            prefix *= nums[i]
        print('answer',answer)
        for i in range(-1,-(length+1),-1):
            answer[i] *= suffix
            suffix *= nums[i]
        return answer
# nums [1, 2, 3, 4]
# answer [1, 1, 2, 6]
# [24, 12, 8, 6]
sobj = Solution()
print(sobj.productExceptSelf([1,2,3,4]))