class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        result = []

        for st in strs:
            sorted_st = ''.join(sorted(st))
            if sorted_st not in seen:
                seen[sorted_st] = []
            seen[sorted_st].append(st)
            
        for key,value in seen.items():
            result.append(value)
        return result
    