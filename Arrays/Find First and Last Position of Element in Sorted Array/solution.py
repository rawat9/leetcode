class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)
        return [left, right]

    def binarySearch(self, data, target, LeftBias):
        low = 0
        high = len(data) - 1
        i = -1
        while low <= high:
            mid = low + (high - low) // 2
            if data[mid] > target:
                high = mid - 1
            elif data[mid] < target:
                low = mid + 1
            else:
                i = mid
                if LeftBias:
                    high = mid - 1
                else:
                    low = mid + 1
        return i
