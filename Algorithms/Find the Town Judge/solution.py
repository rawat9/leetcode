class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if not trust and n == 1: return 1
        people = [0] * (n+1)

        for t in trust:
            people[t[1]] += 1
            people[t[0]] -= 1
            
        return people.index(n-1) if n-1 in people else -1

