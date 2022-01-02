import collections

class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        remainder = collections.defaultdict(int)
        pairs = 0
        for t in time:
            away = t % 60
            pairs += remainder[(60 - away) % 60]
            remainder[away] += 1
        
        return pairs

