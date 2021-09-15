class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        lst = []
        for i in range(1, len(nums)+1):
            total = sum(nums[:i])
            lst.append(total)
        return lst


# Time Complexity = O(N), where N is the length of nums