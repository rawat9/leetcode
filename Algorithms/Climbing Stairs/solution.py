class Solution:
    def climbStairs(self, n: int, memo={}) -> int:
        if n in memo: return memo[n]
        if n < 3: return n

        memo[n] = self.climbStairs(n-1, memo) + self.climbStairs(n-2, memo)
        return memo[n]
