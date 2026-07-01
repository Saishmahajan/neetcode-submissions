class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_list = sorted(list(s1))
        for i in range(len(s2)):
            new_str = s2[i:i+len(s1)]
            if len(new_str) != len(s1):
                continue
            sorted_list = sorted(list(new_str))
            
            if sorted_list == s1_list:
                return True
        return False