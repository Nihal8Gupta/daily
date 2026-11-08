class Solution:
    def numOfStrings(self, patterns: list, word: str) -> int:
        subCount = 0
        for i in patterns:
            if i in word:
                subCount += 1 
        return subCount
sobj = Solution()
word = "abc"
print(sobj.numOfStrings(["a","abc","bc","d"], word))