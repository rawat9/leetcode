class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        Boyer Moore's Voting Algorithm
        """
        count = 0
        candidate = 0

        # Iterate through the array
        for num in nums:

            # candidate <- current num only if count = 0
            if count == 0:
                candidate = num

            count += (1 if num == candidate else -1)

        return candidate, count

# Time Complexity: O(n)
# Space Complexity: O(1)
