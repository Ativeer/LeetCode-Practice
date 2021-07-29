class Solution:
    def countSubstrings(self, s: str) -> int:
        # Expand from the center
        result = 0
        for i in range(len(s)):
            result += self.find_sub(s, i, i)
            result += self.find_sub(s, i , i+1)
        return result
    
    def find_sub(self, st, start, end):
        ans = 0
        while start >= 0 and end < len(st):
            if st[start] != st[end]:
                return ans
            start -= 1
            end += 1
            ans += 1
        return ans
        # TLE
#         def find_sub(s, start, end):
#             while start < end:
#                 if s[start] != s[end]:
#                     return 0
#                 start += 1
#                 end -= 1
#             return 1
        
#         result = 0
#         for i in range(len(s)):
#             for j in range(i, len(s)):
#                 result += find_sub(s, i, j)
#         return result