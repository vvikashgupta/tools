from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.deq = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.deq.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.deq:
            return self.deq.pop()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.deq[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return False if self.deq else True
