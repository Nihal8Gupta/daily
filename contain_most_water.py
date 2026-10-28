def maxArea(heights:list):
    left = 0
    right = len(heights) - 1
    ans = 0
    while left < right:
        ans = max(ans,
                  (min(heights[left],heights[right]) * (right - left)))
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return ans

print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))