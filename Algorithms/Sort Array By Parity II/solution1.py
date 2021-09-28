class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i = 0 # even 
        j = 1 # odd

        while i < len(nums) and j < len(nums):
            if nums[i] % 2 == 0: # if the nums[i] is even
                i += 2
            elif nums[j] % 2 == 1: # if the nums[i] is odd
                j += 2
            else:
                nums[i], nums[j] = nums[j], nums[i]

        return nums