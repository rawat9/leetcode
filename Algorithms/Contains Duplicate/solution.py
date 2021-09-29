class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        # using set() will remove duplicate elements
        return len(nums) != len(set(nums))

# Time Complexity: O(1)