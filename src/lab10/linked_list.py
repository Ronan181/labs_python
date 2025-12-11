class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 
        self._size = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1
    
    def prepend(self, value):
        new_node = Node(value, next=self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self._size += 1

    def insert(self, idx, value):
        if idx < 0 or idx > self._size:
            raise IndexError()

        if idx == 0:
            self.prepend(value)
            return

        if idx == self._size:
            self.append(value)
            return

        current = self.head
        for _ in range(idx - 1):
            current = current.next

        new_node = Node(value, current.next)
        current.next = new_node
        self._size += 1

    def remove_at(self, idx):
        if idx < 0 or idx >= self._size:
            raise IndexError()

        if idx == 0:
            removed = self.head
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return removed.value

        current = self.head
        for _ in range(idx - 1):
            current = current.next

        removed = current.next
        current.next = removed.next

        if removed is self.tail:
            self.tail = current

        self._size -= 1
        return removed.value

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __len__(self):
        return self._size

    def __repr__(self):
        values = list(self)
        return f"SinglyLinkedList({values})"

if __name__=="__main__":
    print("Тесты SinglyLinkedList")

    l = SinglyLinkedList()

    l.append(1)
    l.append(2)
    l.append(3)
    print("После append:", list(l)) 

    l.prepend(0)
    print("После prepend:", list(l))  

    l.insert(2, 99)
    print("После insert:", list(l))
    
    removed = l.remove_at(3)
    print("remove_at(3) вернул:", removed)  
    print("После remove_at:", list(l))  
    print("len:", len(l))
    print("repr:", repr(l))