class Stack_LinkedList:

    class Node:
        __slots__ = 'element', 'next'
        def __init__(self, e) -> None:
            self.element = e
            self.next = None
    
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def first(self):
        if self.is_empty():
            raise Exception("List is Empty")
        return self.head.next

    def enque(self, e):
        node = self.Node(e)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def deque(self):
        node = self.first()
        self.head.next = self.head.next.next
        self.size -= 1
        node.next = None
        return node.element

    def __iter__(self):
        cursor = self.header.next
        while cursor != None:
            yield cursor.element
            cursor = cursor.next



if __name__ == "__main__":
    L = Stack_LinkedList()
    L.enque(5)
    L.enque(6)
    L.enque(7)
    L.enque(8)
    L.enque(9)
    print("Items in Linked List")
    for i in L:
        print(i, end=" ")
    print()
    e = L.deque()
    print(e)
    print("Items in Linked List")
    for i in L:
        print(i, end=" ")
    print()
    L.deque()
    for i in L:
        print(i, end=" ")
    print()
    



        
            




