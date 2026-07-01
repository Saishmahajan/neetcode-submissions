class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq = {}
        left = 0
        max_length = 0
        max_freq = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right],0)+1
            print(freq)
            max_freq = max(max_freq, freq[s[right]])
            print(max_freq)
            while (right - left +1) - max_freq > k:
                freq[s[left]] -= 1
                left+=1
            
            max_length = max(max_length, right - left + 1)

        return max_length
        # max_len = 0

        # for i in range(0, len(s)):
        #     freq = {}
            
        #     for j in range(i,len(s)):
        #         freq[s[j]] = freq.get(s[j], 0) +1
        #         max_freq = max(freq.values())
        #         length = j-i+1
                
        #         if length - max_freq <= k:
        #             max_len = max(max_len, length)
        # return max_len