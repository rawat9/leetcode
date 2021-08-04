class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        i = 0
        j = n

        new_array = []

        while len(new_array) < 2*n:
            new_array.append(nums[i])
            new_array.append(nums[j])
            i += 1
            j += 1

        return new_array

# Time Complexity = O(N)
