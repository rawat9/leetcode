class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()     
        res = []

        for x in range(len(nums)):

			# if previous value is same as current value
            if x > 0 and nums[x] == nums[x-1]:
                continue

            i, j = x + 1, len(nums)-1
            while i < j:
                if nums[x] + nums[i] + nums[j] < 0:
                    i += 1
                elif nums[x] + nums[i] + nums[j] > 0:
                    j -= 1
                else:
                    res.append([nums[x], nums[i], nums[j]])
                    i += 1

					# if the value is still same as previous
                    while i < j and nums[i] == nums[i-1]:
                        i += 1
        return res
