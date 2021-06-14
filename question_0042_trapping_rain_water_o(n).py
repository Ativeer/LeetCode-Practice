class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l_max = [height[0]] * len(height)
        r_max = [height[-1]] * len(height)
        
        for i in range(1, len(height)):
            l_max[i] = max(height[i], l_max[i-1])
        
        for i in range(len(height)-2, -1, -1):
            r_max[i] = max(height[i], r_max[i+1])
        
        water = 0
        for i in range(len(height)):
            h = max(min(r_max[i], l_max[i]) - height[i], 0)
            
            water += h
        return water
            