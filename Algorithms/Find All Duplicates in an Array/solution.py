import collections

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        lst = collections.Counter(nums)
        return [i for i,j in lst.items() if j == 2]
