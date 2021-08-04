class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                return nums[i]

# Time Complexity = O(N)
