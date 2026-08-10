class Solution:
    def maxArea(self, heights: List[int]) -> int:        
        res = []
        if (heights[0] == heights[-1]) and (heights[0] == max(heights)):
            return (heights[0] * (len(heights) - 1))
        left = 0
        right = len(heights) - 1
        val = 0
        while left < right:
            temp = min(heights[left], heights[right]) * (right - left)
            val = max(val, temp)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        res.append(val)
        return (max(res))
