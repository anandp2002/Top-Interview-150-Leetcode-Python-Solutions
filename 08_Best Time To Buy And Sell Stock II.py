class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        profit=0
        for i in range(len(prices)-1):
            profit+=max(0,(prices[i+1]-prices[i]))
        return profit