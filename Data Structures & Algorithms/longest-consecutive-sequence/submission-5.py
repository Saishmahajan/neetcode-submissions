class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums1 = list(set(nums))
        nums1 = sorted(nums1)
        c = 1
        counter = []
        if len(nums1) == 0:
                return 0
        for i in range(0,len(nums1)-1):
                if nums1[i] +1 ==  nums1[i+1]:
                        c += 1
                        counter.append(c)
                else :
                        c = 1
        if len(counter) == 0:
                return 1
        return max(counter)