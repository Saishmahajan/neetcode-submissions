class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0 
        length = 0
        width = 0



        for i in range(0,len(heights)):
            for j in range(i+1, len(heights)):
                length = min(heights[i],heights[j])
                width = j - i
                area = length * width
                
                max_area = max(max_area, area)
                
        return max_area