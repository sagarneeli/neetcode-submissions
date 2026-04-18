class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                current_area = min(heights[i], heights[j]) * (j - i)
                max_water = max(max_water, current_area)
        
        return max_water

        