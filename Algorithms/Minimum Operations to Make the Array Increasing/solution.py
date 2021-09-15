class Solution:
    def minOperations(self, nums: list[int]) -> int:
        oper = 0
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                a = (nums[i]+1) - nums[i+1]
                nums[i+1] += a
                oper += a
        return oper

# Time Complexity = O(N)