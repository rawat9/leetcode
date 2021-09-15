class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

# Time Complexity = O(1)