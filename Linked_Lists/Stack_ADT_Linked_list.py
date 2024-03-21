class Stack_LinkedList:

    class Node:
        __slots__ = 'element', 'next'
        def __init__(self, e) -> None:
            self.element = e
            self.next = None
    
    def __init__(self) -> None:
        self.head = None
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def first(self):
        if self.is_empty():
            raise Exception("List is Empty")
        return self.head

    def push(self, e):
        node = self.Node(e)
        if self.is_empty():
            self.head  = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        node = self.first()

        self.head = self.head.next
        self.size -= 1
        node.next  = None
        return node.element

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.element
    
    def display(self):
        if self.is_empty():
            return None
        print("Items in single Linked list: ")
        
        walk = self.head
        while walk != None:
            print(walk.element, end=" ")
            walk = walk.next
        print()


        

    def __iter__(self):
        cursor = self.head
        
        while cursor != None:
            yield cursor.element
            cursor = cursor.next
    
    def reverse(self):
        if self.is_empty():
            return None
        
        prev = None
        
        curr = self.head
        while curr != None:
            next  = curr.next
            curr.next =  prev
            prev = curr
            curr = next
        
        self.head = prev
        return

        # return self._reverse(self.head)
    
    def _reverse(self, node):
        if node.next is None:
            self.head = node
            return node

        reversed_node = self._reverse(node.next)

        node.next.next = node
        node.next = None
        return node




if __name__ == "__main__":
    L = Stack_LinkedList()
    L.push(5)
    L.push(6)
    L.push(7)
    L.push(8)
    L.push(9)
    L.push(2)
    L.display()
    L.reverse()
    L.display()
   