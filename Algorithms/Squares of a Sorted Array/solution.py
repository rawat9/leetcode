class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        squares = list(map(lambda x: x**2, nums))
        return sorted(squares)

# Time Complexity = O(1)