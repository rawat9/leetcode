class Solution:
	def longestMountain(self, arr: list[int]) -> int:
		base = res = 0
		N = len(arr)
		
		while base < N:
			end = base

			# if base is left boundary of mountain
			if end + 1 < N and arr[end] < arr[end+1]:

				# set end to peak of current mountain
				while end + 1 < N and arr[end] < arr[end+1]:
					end += 1
				
				# if end -> peak? 
				if end + 1 < N and arr[end] > arr[end+1]:

					# set end to right boundary of mountain
					while end + 1 < N and arr[end] > arr[end+1]:
						end += 1
					
					# length of the mountain is recorded
					res = max(res, end - base + 1)
					
			# set new base -> end
			base = max(end, base + 1)
			
		return res

sol = Solution()
print(sol.longestMountain([1, 2, 3, 2, 1, 0, 2, 3, 1]))

# Time Complexity - O(N)
# Space Complexity - O(1)
