class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        n = len(s)
        res = [""] * n

        for i in range(len(indices)):
            res[indices[i]] = s[i]

        return "".join(res)
