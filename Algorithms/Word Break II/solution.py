class Solution:
    def __init__(self):
        self.memo = {}
        
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        if s in self.memo:
            return self.memo[s]

        if s == "":
            return [""]

        result = []

        for word in wordDict:
            if s.find(word) == 0:
                suffix = s[len(word):]
                suffixWays = self.wordBreak(suffix, wordDict)
                for way in suffixWays:
                    result.append((' '.join([word,way])).strip())

        self.memo[s] = result
        return result

