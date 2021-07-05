from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            t = sorted(s)
            x = "".join(i for i in t)
            
            res[x].append(s)
        return res.values()