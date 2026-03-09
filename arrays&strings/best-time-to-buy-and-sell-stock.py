class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        mini, maxi = prices[0], prices[0]
        for i in prices:
            mini = min(mini, i)
            profit = max(profit, i - mini)
        return profit