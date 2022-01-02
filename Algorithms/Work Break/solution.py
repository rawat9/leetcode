class Solution:
    def __init__(self):
        self.memo = {}
        
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        if s in self.memo:
            return self.memo[s]
        
        if s == "":
            return True
        
        for word in wordDict:
            if s.find(word) == 0:
                suffix = s[len(word):]
                if self.wordBreak(suffix, wordDict) == True:
                    self.memo[s] = True
                    return True
                
        self.memo[s] = False
        return False
                
