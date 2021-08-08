# Backtracking TLE
class Solution:

    def minCut(self, s: str) -> int:
        
        def checkPalindrome(s, start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        def findPartition(s, start, end, partitions):
            
            if start == end or checkPalindrome(s, start, end-1):
                return 0
            
            for i in range(start, end):
                
                if checkPalindrome(s, start, i):
                    partitions = min(partitions, 1+ findPartition(s, i+1, end, partitions))
            return partitions
        return findPartition(s, 0, len(s), len(s))



# Expand From Center:

class Solution:
    def minCut(self, s: str) -> int:
        dp = [i for i in range(len(s))]
        
        def expandAroundCenter(start, end, s, dp):
            while start >=0 and end < len(s) and s[start] == s[end]:
                if start == 0:
                    n = 0
                else:
                    n = dp[start-1] + 1
                dp[end] = min(dp[end], n)
                start -= 1
                end += 1
        
        for mid in range(len(s)):
            expandAroundCenter(mid, mid, s, dp)
            expandAroundCenter(mid-1, mid, s, dp)
            
        return dp[-1]