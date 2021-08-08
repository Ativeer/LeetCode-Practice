class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        a = s.split(" ")
        for i in range(len(a)-1, -1, -1):
            if a[i] == "":
                continue
            else:
                ans += a[i]
                ans += " "
        return ans[:-1]