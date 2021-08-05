class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        ht = dict()

        for i in range(len(nums)):
            if nums[i] in ht:
                return [ht[nums[i]], i]
            else:
                ht[target - nums[i]] = i


# Time Complexity = O(N)