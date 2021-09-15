class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._items = []       

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self._items.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self._items.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self._items[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self._items) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()