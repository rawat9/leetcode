class Solution:
    def distance(self, point):
        return point[0] ** 2 + point[1] ** 2

    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        points.sort(key=self.distance) 
        return points[:k]
