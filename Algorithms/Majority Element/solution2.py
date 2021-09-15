class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

# Time Complexity: O(nlogn) why? sorting costs nlogn time
