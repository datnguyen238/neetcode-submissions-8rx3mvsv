class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        
        max_vol = 0
        l, r = 0, len(heights)-1

        while l < r:
            width = r - l
            current_vol = min(heights[l], heights[r]) * width
            max_vol = max(current_vol, max_vol)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_vol
            