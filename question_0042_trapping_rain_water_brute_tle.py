class Solution:
    def trap(self, height: List[int]) -> int:
        # brute force
        maxx = []
        for i in range(1, len(height)-1):
            # right_max
            r_max = height[0]
            for r in range(0, i):
                r_max = max(r_max, height[r])
            
            
            l_max = height[i+1]
            for l in range(i+1, len(height)):
                l_max = max(l_max, height[l])
                
            maxx.append((r_max, l_max))
        
        water = 0
        
        for points in range(len(maxx)):
            if maxx[points][0] <= height[points+1] or maxx[points][1] <= height[points+1]:
                continue
            water += (min(maxx[points][0], maxx[points][1]) - height[points+1])
        return water