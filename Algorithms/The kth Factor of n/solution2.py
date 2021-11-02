class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        i = 1
        while i * i <= n:
            if n % i == 0:
                factors.append(i)
                if (n//i) != i:
                    factors.append(n//i)
            i += 1 
        factors.sort()
        return factors[k-1] if k-1 < len(factors) else -1
