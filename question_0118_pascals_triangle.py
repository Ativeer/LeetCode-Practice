class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans = []
        prev = [1]
        ans.append(prev)
        for i in range(numRows-1):
            curr = []
            n = len(prev) + 1
            for i in range(n):
                if i == 0:
                    curr.append(prev[i])
                elif i == n-1:
                    curr.append(prev[-1])
                else:
                    curr.append(prev[i-1]+prev[i])
            ans.append(curr)
            prev = curr
        return ans