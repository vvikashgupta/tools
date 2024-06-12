from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.deq = deque(maxlen=size)
        self.maxlen = size

    def next(self, val: int) -> float:
        self.deq.append(val)
        deq_len = len(self.deq)
        return sum(self.deq)/float(deq_len)
