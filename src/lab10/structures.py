from collections import deque


class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if not self._data:
            raise IndexError()
        return self._data.pop()

    def peek(self):
        if not self._data:
            return None
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)


class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if not self._data:
            raise IndexError()
        return self._data.popleft()

    def peek(self):
        if not self._data:
            return None
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

if __name__=="__main__":
    s = Stack()

    print("Stack tests:")
    print("Is empty:", s.is_empty())  # True

    s.push(10)
    s.push(20)
    s.push(30)

    print("Peek:", s.peek())  # 30
    print("Pop:", s.pop())    # 30
    print("Pop:", s.pop())    # 20
    print("Len:", len(s))  # 1
    print("Is empty:", s.is_empty())  # False
    print()



    q = Queue()

    print("Queue tests:")
    print("Is empty:", q.is_empty())  # True

    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")

    print("Peek:", q.peek())  # a
    print("Dequeue:", q.dequeue())  # a
    print("Dequeue:", q.dequeue())  # b
    print("Len:", len(q))  # 1
    print("Is empty:", q.is_empty())  # False
    print()