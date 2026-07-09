class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # new_arr = []

        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         new_arr.append(matrix[i][j])
                
                
        # if target in new_arr:
        #     return True
        # else:
        #     return False

        rows = len(matrix)
        columns = len(matrix[0])
        low = 0
        high = rows*columns - 1

        while low <= high:
            
            mid = low+(high-low)//2
            rows = mid // columns
            col = mid % columns
            value = matrix[rows][col]
            
            if value ==  target:
                return True
            if value < target:
                low = mid + 1
            if value > target : 
                high = mid  -1
            
        return False