import collections

class Solution:
    def frequencySort(self, s: str) -> str:
        res = ""
        sorting = collections.Counter(s)        
        for i, j in sorted(sorting.items(), key=lambda x: x[1], reverse=True):
            if j > 1:
                res += i * j
            else:
                res += i
        return res
