class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        intersection = []
        for i in nums2:
            if i in nums1:
                intersection.append(nums1.pop(nums1.index(i)))
        return intersection

