class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        pairs = [(x,y) for x,y in zip(spaces[:-1], spaces[1:])]
        pairs.insert(0, (0, spaces[0]))
        pairs.append((spaces[-1], len(s)))
        return " ".join([s[i:j] for i, j in pairs])
