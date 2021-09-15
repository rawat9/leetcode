class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = list(map(lambda x: True if x+extraCandies >=
                          max(candies) else False, candies))
        return result

# Time Complexity = O(1)