class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.f = 0
        self.r = 0

    def enQueue(self, value: int) -> bool:
        if not self.q[self.r]:
            self.q[self.r] = value
            self.r = (self.r +1) % self.maxlen
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.q[self.f]:
            return False
        else:
            self.q[self.f] = None
            self.f = (self.f + 1) % self.maxlen
            return True

    def Front(self) -> int:
        return -1 if not self.q[self.f] else self.q[self.f]

    def Rear(self) -> int:
        return -1 if not self.q[self.r] else  self.q[self.r-1]

    def isEmpty(self) -> bool:
        return 1 if not (self.q[self.f] and self.q[self.r]) else 0

    def isFull(self) -> bool:
        return 1 if self.f == self.r and self.q[self.f] else 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()