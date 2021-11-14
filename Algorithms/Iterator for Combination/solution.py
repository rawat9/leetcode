from itertools import combinations


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combinations = ["".join(c) for c in combinations(characters, combinationLength)]
        self.index = -1
        
    def next(self) -> str:
        self.index += 1
        return self.combinations[self.index]

    def hasNext(self) -> bool:
        return self.index < len(self.combinations) - 1


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()