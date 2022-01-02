class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return str(num) == str(num).rstrip("0") or num == 0
