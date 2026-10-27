class Solution:

    def findTwoSum(self,nums:list,target:int):
        length = len(nums)
        for i in range(length):
            for j in range(i,length):
                if target == nums[i] + nums[j]:
                    return [i,j]
        return -1

    def findTwoSumByHashMap(self,nums:list,target:int):
        seen = {}
        for i,num in enumerate(nums):
            check = target - num
            if check in seen:
                return [seen[check],i]

            seen[num] = i
        return -1

sobj = Solution()
print(sobj.findTwoSum([2,4,8,1,5,7],9))
print(sobj.findTwoSumByHashMap([2,4,8,2,5,7],9))