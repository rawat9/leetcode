class Solution:
    def __init__(self):
        self._items = []
    
    def push(self, value):
        self._items.append(value)
        
    def pop(self):
        return self._items.pop()
    
    def isEmpty(self):
        return len(self._items) == 0
        
    def isValid(self, s: str) -> bool:
        lefty = '({['
        righty = ')}]'
        for char in s:
            if char in lefty:
                self.push(char)
            elif char in righty:
                if self.isEmpty():
                    return False
                if righty.index(char) != lefty.index(self.pop()):
                    return False
        
        return self.isEmpty()


# Time Complexity = O(n)