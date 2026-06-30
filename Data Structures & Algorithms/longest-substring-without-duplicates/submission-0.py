class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_len = 0

                    
        for i in range(len(s)):
            seen = []
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                seen.append(s[j])

                curr_len = j - i + 1
                max_len = max(max_len,curr_len)
        return max_len