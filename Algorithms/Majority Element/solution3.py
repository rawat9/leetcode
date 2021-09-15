import collections


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Mapping elements to their respective count
        elements = collections.Counter(nums)

        # return the key with maximum value
        return max(elements.keys(), key=elements.get)
