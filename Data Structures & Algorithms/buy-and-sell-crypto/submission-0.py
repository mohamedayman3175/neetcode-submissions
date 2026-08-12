class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        best = 0

        for right in range(len(prices)):
            window_profit = prices[right] - prices[left]

            if prices[right] < prices[left]:
                left = right

            best = max(best, window_profit)
        return best
                