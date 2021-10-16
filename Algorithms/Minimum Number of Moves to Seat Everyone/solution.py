class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        total = 0
        for x,y in zip(sorted(seats), sorted(students)):
            total += abs(x-y)

        return total
