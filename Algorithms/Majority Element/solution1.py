class Solution:
    def majorityElement(self, nums: List[int]) -> int:
		# removing the duplicates
        set1 = list(set(nums))  
        n = len(set1)

		# iterating through the array 
		# find the count of each duplicate item i.e set1[i] in the entire nums[]

        for i in range(n):
            if nums.count(set1[i]) > (len(nums) / 2):
                return set1[i]


# Time Complexity: O(n)