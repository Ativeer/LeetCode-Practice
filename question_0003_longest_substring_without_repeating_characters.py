class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        start_pos = 0
        m = 0
        count = 0
        for pos, char in enumerate(s):            
            if char in d:
                p = d[char][1]
                if start_pos <= p:
                    m = max(m, count)
                    count = pos - p - 1
                    start_pos = p + 1
            count += 1
            d[char] = [1, pos]
        
        return max(m, count)