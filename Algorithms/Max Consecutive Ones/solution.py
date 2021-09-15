class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        most = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            elif nums[i] != 1:
                count = 0

            most = max(most, count)

        return most


# Time Complexity = O(N)