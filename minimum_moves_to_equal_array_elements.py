def minMoves(nums: list[int]) -> int:
    minimum = min(nums)
    moves = 0
    for num in nums:
        moves += num - minimum
    
    return moves

print(minMoves([1,2,3]))