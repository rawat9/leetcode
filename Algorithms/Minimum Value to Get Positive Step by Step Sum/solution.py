class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        min_value, total = 0, 0

        for num in nums:
            total += num
            min_value = min(total, min_value)

        return -min_value + 1
