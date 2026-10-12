class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = float("-inf")
        while r < len(prices):
            sell = prices[r] - prices[l]
            if sell > profit:
                profit = sell 

            if prices[r] > prices[l]:
                r += 1
            else:
                l = r
                r += 1
        if profit <= 0:
            return 0
        return profit

        