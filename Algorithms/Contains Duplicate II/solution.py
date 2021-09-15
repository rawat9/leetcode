class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        ht = {}

        for i in range(len(nums)):

			# check if the element already exists
			# below condition will not be true until 
			# first duplicate enters the array
            if nums[i] in ht and abs(i - ht[nums[i]]) <= k:
                return True
            ht[nums[i]] = i

        return False


# Time Complexity: O(n)
