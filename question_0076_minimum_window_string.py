from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s, t):
        if not t or not s:
            return ""

        set_t = Counter(t)
        unique = len(set_t)
        start, end = 0, 0
        tchar_count = 0
        window_counts = defaultdict(int)
        min_len = len(s)+1
        window_start = 0
        window_end = 0
        while end < len(s):
            character = s[end]
            window_counts[character] += 1
            if character in set_t and window_counts[character] == set_t[character]:
                tchar_count += 1
            while start <= end and tchar_count == unique:
                character = s[start]
                if end - start + 1 < min_len:
                    min_len = end - start + 1
                    window_start = start
                    window_end = end

                window_counts[character] -= 1
                if character in set_t and window_counts[character] < set_t[character]:
                    tchar_count -= 1
                start += 1

            end += 1
        return "" if min_len == len(s)+1 else s[window_start : window_end + 1]


# NAIVE APPROACH

# O(n^2)

# from collections import Counter
# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if len(t) > len(s):
#             return ""
#         set_t = Counter(t)
#         temp = Counter(t)
#         min_str = s + "0"
#         min_length = len(min_str)
        
#         for chars in range(len(s)):
            
#             if s[chars] in temp:
                
#                 if temp[s[chars]] == 0:
#                     continue
#                 ans = ""
#                 for i in range(chars, len(s)):
#                     if s[i] in temp:
#                         temp[s[i]] -= 1
#                         if temp[s[i]] == 0:
#                             del temp[s[i]]
#                     ans += s[i]
                    
#                     if not temp:
#                         break
#                 if not temp:
#                     l = len(ans)
#                     min_str = ans if l < min_length else min_str
#                     min_length = min(min_length, l)
#                 temp = set_t.copy()
                
#         return min_str if min_str[-1] != "0" else ""

