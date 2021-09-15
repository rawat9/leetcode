class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                profit = prices[j] - prices[i]
                if profit > max_profit:
                    max_profit = profit

        return max_profit

# Time Complexity = O(n^2)
