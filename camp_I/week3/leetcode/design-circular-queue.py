class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.elements = [0] * k
        self.front = 0
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False

        self.rear += 1
        self.rear %= self.capacity
        self.elements[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        self.front += 1
        self.front %= self.capacity
        self.size -= 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.elements[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.elements[self.rear]

    def isEmpty(self) -> bool:
        return not self.size

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()