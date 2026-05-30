class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(0, len(numbers)):
        #         for j in range(i+1, len(numbers)):
        #                 if numbers[i] + numbers[j] == target:
        #                          return [i+1,j+1]
            
        l = 0
        r = len(numbers)-1

        while l < r : 
                sums = numbers[l] + numbers[r]
                if sums == target:
                        return [l+1, r+1]
                if sums > target :
                        r -= 1
                if sums < target:
                        l += 1