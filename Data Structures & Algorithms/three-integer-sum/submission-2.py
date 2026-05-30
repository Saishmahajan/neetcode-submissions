class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
#        dont use this interviewer marega
        # numset = list(set(nums))
        # result = []

        # for i in range(0,len(numset)):
        #         for j in range(i+1, len(numset)):
        #                 for k in range(i+2, len(numset)):
        #                         if numset[i] +numset[j] + numset[k] == 0:
        #                                 result.append([numset[i] ,numset[j] , numset[k]])
                
        # return result

        numset =  sorted(nums)
        result = []
        print(numset)

        for i in range(len(numset)):
        
                l = i+1
                r = len(numset)-1
                if i > 0 and numset[i] == numset[i-1]:
                        continue
                
                while l <r:
                        
                        if numset[i] + numset[l] + numset[r] == 0:
                                result.append([numset[i], numset[l], numset[r]]) 
                                r -= 1
                                l += 1
                        elif numset[i] + numset[l] + numset[r] > 0:
                                r -= 1
                        elif numset[i] + numset[l] + numset[r] < 0 :
                                l += 1
        unique = list(set(tuple(x) for x in result))

        # If you want back as list of lists
        unique = [list(x) for x in unique]

        return unique