class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #using division operator
        # product = 1
        # result = []
        # for i in nums:
        #     product *= i
        # print(product)
        # for i in nums:
        #     result.append(product // i)
            
        # print(result)
        # nums = [1,2,4,6]

        #without using division operator 
        # ------->
        # 1, 1, 1, 1
        # prefix = 1
        # 0th iteration : 1, 1, 1, 1.  prefix = 1*1 = 1
        # 1th iteration : 1, 1, 1, 1   prefix = 1*2 = 2
        # 2nd iteration : 1, 1, 2, 1   prefix = 2*4 = 8
        # 3rd iteration : 1, 1, 2, 8   prefix = 8*6 = 48


        # <-------
        # 1, 1, 2, 8
        # suffix = 1
        # 0th iteration : 1, 1, 2, 8*1  suffix = 1*6 = 6
        # 1st iteration : 1, 1, 2*6, 8  suffix = 6*4 = 24
        # 2nd iteration : 1, 1*24, 12, 8 suffix = 24*2 = 48
        # 3rd iteration : 1*48, 24, 12, 8 suffix = 48*1 = 48
                                                                                                                
        ans = [1]*len(nums)

        prefix = 1

        for i in range(len(nums)):
                ans[i] = prefix
                prefix *= nums[i]
        
        suffix = 1   
        for i in range(len(nums)-1, -1, -1):
                ans[i] *= suffix
                suffix *= nums[i]
        
        return ans