# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:
# [1,2,3,4,5,6,7, 8 ,9,10] # res = 8

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            mid = low + (high - low) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res > 0:
                low = mid + 1
            else:
                high = mid - 1
        return -1
