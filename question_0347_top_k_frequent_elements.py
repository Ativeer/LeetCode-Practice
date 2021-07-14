# Sorting
# N*log(N)
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = defaultdict(int)
        for i in nums:
            ans[i] += 1
        return list({k:v for k, v in sorted(ans.items(), key=lambda item: item[1], reverse=True)}.keys())[:k]


# Heaps
# N*log(K)
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)

# BUCKET SORTING
# O(N)
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        ans = [[] for _ in range(len(nums))]
        
        for c in count:
            ans[count[c]-1].append(c)
        res = []
        
        for i in range(len(nums)-1, -1, -1):
            
            if ans[i] == []:
                continue
            else:
                counter = 0
                while k > len(res) and counter < len(ans[i]):
                    res.append(ans[i][counter])
                    
                    counter += 1
                if k == len(res):
                    return res
        return res
