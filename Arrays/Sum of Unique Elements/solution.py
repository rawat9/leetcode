class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        unique = 0
        if len(nums) == 1:
            return nums[0]
        for i in range(0, len(nums)):
            if nums[i] != nums[i-1] and nums.count(nums[i]) == 1:
                unique += nums[i]
        return unique


# Time Complexity = O(N)