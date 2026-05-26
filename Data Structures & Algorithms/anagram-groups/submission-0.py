from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapped = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            mapped[key].append(word)

        return list(mapped.values())