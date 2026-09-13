class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0

        i = 0
        n = len(prices)

        while i < n:
            buy = prices[i]
            j = i + 1
            while j < n:
                sell = prices[j]
                max_profit = max(max_profit,  sell - buy)
                j += 1
            i += 1
        return max_profit
