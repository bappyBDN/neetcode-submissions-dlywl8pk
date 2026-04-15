class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Max_profit =0
        n=len(prices)
        for i in range(n-1):
            for j in range(i+1,n):
                c_sum=prices[j]-prices[i]
                Max_profit = max(Max_profit,c_sum)
        return Max_profit
        