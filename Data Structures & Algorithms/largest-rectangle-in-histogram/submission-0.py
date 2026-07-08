class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0

        for i in range(0,len(heights)):
            min_height = float('inf')
            for j in range(i, len(heights)):
                min_height = min(min_height,heights[j])
                width = j - i + 1
                area = min_height * width 
                max_area = max(max_area, area)
                

        return max_area
