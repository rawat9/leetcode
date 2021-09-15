class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if target not in nums:
                if target > max(nums):
                    return nums.index(max(nums)) + 1
                elif target < nums[i]:
                    return i
            else:
                return nums.index(target)

# Time Complexity = O(N)
