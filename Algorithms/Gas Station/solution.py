class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total, curr = 0, 0
        start = 0
        diff = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            curr += diff

            if curr < 0:
                start = i + 1
                curr = 0
        
        if total >= 0:
            return start

        return -1
