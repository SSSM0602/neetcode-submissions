class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        maxWater = 0
        while l < r:
            water = (r - l)*min(heights[l], heights[r])
            if water > maxWater:
                maxWater = water
            
            if heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return maxWater

                
            
            
        