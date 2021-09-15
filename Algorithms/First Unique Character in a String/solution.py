class Solution:
    def firstUniqChar(self, s: str) -> int:
        hmap = {}
    
        for i in range(len(s)):
            hmap[s[i]] = i
            if s.count(s[i]) == 1:
                return i
        return -1 


# Time Complexity - O(n)
