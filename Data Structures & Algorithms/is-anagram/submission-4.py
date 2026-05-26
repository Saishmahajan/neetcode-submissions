class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # list1 = sorted(list(s))
        # list2 = sorted(list(t))
        

        # if len(list1) != len(list2):
        #     return False

        # for i in range(0,len(list1)):
        #     if list1[i] != list2[i]:
        #         return False
        # return True

        return sorted(s) == sorted(t)