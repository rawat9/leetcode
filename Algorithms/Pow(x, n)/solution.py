class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        return [num for num in nums if nums.count(num) == 1]