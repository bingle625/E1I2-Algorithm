# 25번 원형 큐 디자인

class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0
        self.p2 = 0

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.q[self.p2] is None:
            self.q[self.p2] = value
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        else:
            return False

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.q[self.p1] is None:
            return False
        else:
            self.q[self.p1] = None
            self.p1 = (self.p1+1) % self.maxlen
            return True

    def Front(self):
        """
        :rtype: int
        """
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    def Rear(self):
        """
        :rtype: int
        """
        return -1 if self.q[self.p2-1] is None else self.q[self.p2 - 1]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self):
        """
        :rtype: bool
        """
        return self.p1 == self.p2 and self.q[self.p1] is not None

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
