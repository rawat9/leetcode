class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._items = []

    def push(self, val: int) -> None:
        self._items.append(val)

    def pop(self) -> None:
        return self._items.pop()

    def top(self) -> int:
        return self._items[-1]

    def getMin(self) -> int:
        return min(self._items)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()