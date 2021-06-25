class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        t = 0
        j = len(height)-1
        m = 0
        while j > i:
            m = max(m, min(height[i], height[j])*(j-i))
            t += (height[i]<=height[j])
            j -= (height[i]>height[j])
            i = t
        return m