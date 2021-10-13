class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_size = float('inf')
        start = 0
        curr_sum = 0
        for end, val in enumerate(nums):
            curr_sum += val

            while curr_sum >= target:
                # minimal length comparision
                min_size = min(min_size, end - start + 1)

                # decrease the window size from the start
                curr_sum -= nums[start] 
                start += 1

        return min_size if min_size != float('inf') else 0
