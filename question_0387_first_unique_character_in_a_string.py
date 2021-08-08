class Solution:
    def firstUniqChar(self, s: str) -> int:
        a = [-1 for _ in range(26)]
        for i in range(len(s)-1, -1, -1):
            pos = ord(s[i])-97
            if a[pos] != -1:
                a[pos] = -2
            else:
                a[pos] = i
        
        m = len(s) + 1
        for i in range(26):
            if a[i] > -1:
                m = min(m, a[i])
        return m if m != len(s) + 1 else -1