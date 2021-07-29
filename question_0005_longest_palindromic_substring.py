class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Expand from center
        if not s:
            return ""
        def expandFromCenter(s, start, end):
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            return end - start - 1
        
        start = 0
        end = 0
        for i in range(len(s)):
            # odd length
            l1 = expandFromCenter(s, i, i)
            # even length
            l2 = expandFromCenter(s, i, i+1)
            ans = max(l1, l2)
            if ans > (end-start):
                start = i - (ans - 1)//2
                end = i + ans//2
        return s[start:end+1]