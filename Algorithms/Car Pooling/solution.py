class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        stops = []
        for ppl, start, end in trips:
            stops.append((start, ppl))
            stops.append((end, -ppl))

        stops.sort()

        for _, p in stops:
            capacity -= p

            if capacity < 0:
                return False

        return True

