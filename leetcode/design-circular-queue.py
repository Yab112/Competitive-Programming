class Node:
    def __init__(self, value):
        self.next = None
        self.val = value

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.head = None
        self.tail = None

    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            new_node = Node(value)
            if not self.head:
                self.head = new_node
            else:
                self.tail.next = new_node
            self.tail = new_node
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return True
        else:
            return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.head.val
        else:
            return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.tail.val
        else:
            return -1

    def isEmpty(self) -> bool:
        return not self.head

    def isFull(self) -> bool:
        if not self.head:
            return False

        count = 1
        cur = self.head.next
        while cur != None:
            count += 1
            cur = cur.next

        return count == self.k

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
