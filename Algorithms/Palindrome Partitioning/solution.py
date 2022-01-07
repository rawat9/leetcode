class Solution:
    def partition(self, s: str) -> list[list[str]]:
        def isPalindrome(start, end):
            while start <= end:
                if s[start] != s[end]: 
                    return False
                start += 1
                end -=1
            return True
        
        def dfs(start, path):
            if start >= len(s): 
                self.result.append(path)
                
            for p in range(len(s) - start):
                if isPalindrome(start, start + p):
                    dfs(start + p + 1, path + [s[start:start + p + 1]])
        
        self.result = []
        dfs(0, [])
        return self.result
