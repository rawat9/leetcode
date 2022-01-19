class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:    
        i, count = 0, 0
        N = len(flowerbed)
        while i < N:
            if flowerbed[i] == 0 and (i == N-1 or flowerbed[i+1] == 0) and (i == 0 or flowerbed[i-1] == 0):
                flowerbed[i] = 1
                count += 1
            i += 1
        return count >= n

