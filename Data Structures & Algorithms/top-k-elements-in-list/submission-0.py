class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = 0
        result = []

        mydict = {}

        for i in sorted(nums) :
            mydict[i] = mydict.get(i,0)+1
            
        new = sorted(mydict.items(),key=lambda x : x[1], reverse=True)
        for i in new[:k]:
            result.append(i[0])

        return result
