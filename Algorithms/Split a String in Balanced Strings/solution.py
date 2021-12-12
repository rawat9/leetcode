class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        count = 0
        
        for i in range(len(s)):
            if s[i] == 'R':
                balance += 1
            elif s[i] == 'L':
                balance -= 1
            
            if balance == 0:
                count += 1

        return count