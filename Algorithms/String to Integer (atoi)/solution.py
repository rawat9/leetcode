class Solution:
    def myAtoi(self, s: str) -> int:
        MIN, MAX = -2 ** 31, 2 ** 31 - 1
        n, empty, sign = 0, True, +1
        
        for char in s:
            
            # handle special cases
            if empty:
                if char == ' ':
                    continue
                elif char == '-':
                    sign = -1
                elif char.isdigit(): 
                    n = int(char)  
                elif char != '+':
                    return 0
                empty = False
            else:
                if char.isdigit():
                    n = n * 10 + int(char)
                    if sign * n > MAX: 
                        return MAX
                    elif sign * n < MIN: 
                       return MIN
                else: break   # end of valid number
        
        return sign * n  
 
