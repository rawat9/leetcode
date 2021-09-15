class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        digits = list(map(lambda x: len(str(x)), nums))

        count = 0
        for i in range(len(digits)):
            if digits[i] % 2 == 0:
                count += 1
        return count

# Time Complexity = O(N), where N is the length of nums