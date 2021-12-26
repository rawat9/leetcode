class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sumOfDigits = 0
        product = 1
        while n > 0:
            mod = n % 10
            n = int(n - mod) // 10
            sumOfDigits += mod
            product *= mod
            
        return product - sumOfDigits
            