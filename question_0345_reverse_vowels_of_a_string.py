class Solution:
    def reverseVowels(self, s: str) -> str:
        start = 0
        end = len(s) - 1
        vowels = ['a','e','i','o','u', 'A', 'E','I','O','U']
        L = list(s)
        while start <= end:
            while start <= end and s[start] not in vowels:
                start += 1
            while end>= start and s[end] not in vowels:
                end -= 1
            if start <= end:
                L[start], L[end] = L[end], L[start]
                start += 1
                end -= 1
        return "".join(L)