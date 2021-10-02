import numpy as np

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        try:
            result = np.reshape(np.array(original), (m,n))       
            return result
        except ValueError:
            return []