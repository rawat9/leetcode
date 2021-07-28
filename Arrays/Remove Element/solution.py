class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        n = len(nums)
        j = 0
        for i in range(0, n):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j
