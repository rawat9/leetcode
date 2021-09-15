class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        minimum = max(prices)

        for i in range(len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - minimum)

        return max_profit

# Time Complexity = O(n)