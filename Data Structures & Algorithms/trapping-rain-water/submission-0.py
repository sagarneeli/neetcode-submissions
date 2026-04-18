class Solution:
    def trap(self, height: List[int]) -> int:
        curr_max = 0
        prefix = []
        for h in height:
            curr_max = max(curr_max, h)
            prefix.append(curr_max)
        
        curr_max = 0
        suffix = []
        i = 0
        for h in height[::-1]:
            curr_max = max(curr_max, h)
            suffix.insert(-i, curr_max)
            i += 1
        
        max_water_area = 0

        for i in range(len(height)):
            max_water_area += min(prefix[i], suffix[i]) - height[i]
        
        return max_water_area
        