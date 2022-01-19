class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words, hmap = s.split(), {}
        
        if len(words) != len(pattern) or len(set(words)) != len(set(pattern)): 
            return False
        
        for i in range(len(words)):
            if words[i] not in hmap:
                hmap[words[i]] = pattern[i]
            elif hmap[words[i]] != pattern[i]:
                return False

        return True
