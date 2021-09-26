import math

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
    
        result = math.log(abs(n), 3) 
        return True if n == pow(3, round(result)) else False
