class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        buy_ptr = 0
        i = 1
        while i < len(prices):
            
            if prices[i-1] > prices[i]:
                p += prices[i-1] - prices[buy_ptr]
                while prices[i-1] >= prices[i]:
                    i += 1
                    if i == len(prices):
                        return p
                buy_ptr = i-1
            else:
                i += 1
        p += prices[-1] - prices[buy_ptr]
        return p