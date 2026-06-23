class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        for i in range(len(prices)):
            mi = min(prices)

            if mi == prices[-1]:
                return 0

            indx = prices.index(mi)
            ma = max(prices[indx:])

            profit = ma - mi
            if profit > 0:
                return profit
            return 0