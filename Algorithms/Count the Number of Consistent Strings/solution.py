class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        count = 0
        for word in words:
            if len(set(word).difference(allowed)) == 0:
                count += 1
                
        return count