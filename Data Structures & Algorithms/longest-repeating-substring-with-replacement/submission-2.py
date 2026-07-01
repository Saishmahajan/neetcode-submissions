class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0

        for i in range(0, len(s)):
            freq = {}
            
            for j in range(i,len(s)):
                freq[s[j]] = freq.get(s[j], 0) +1
                max_freq = max(freq.values())
                length = j-i+1
                
                if length - max_freq <= k:
                    max_len = max(max_len, length)
        return max_len