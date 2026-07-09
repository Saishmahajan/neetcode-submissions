class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        new_arr = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                new_arr.append(matrix[i][j])
                
                
        if target in new_arr:
            return True
        else:
            return False
    