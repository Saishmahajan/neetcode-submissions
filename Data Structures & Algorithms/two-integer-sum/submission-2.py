class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(0,len(nums)):

        #     if target - nums[i] in nums:
        #         return [i, nums.index(target-nums[i])]

        seen = {}

        for i,num in enumerate(nums):
            
            if target - num in seen:
                return [seen[target - num],i] 
            else : 
                seen[num] = i
            