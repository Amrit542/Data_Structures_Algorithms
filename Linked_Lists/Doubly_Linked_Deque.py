from Doubly_Linked_Base import _DoublyLinkedBase

class DoublyLinkedDeque( _DoublyLinkedBase ):
    """Doubly-ended queue implementation based on a doubly linked list."""

    def first(self):
        """Return (but do not remove) the element at the front of the deque."""
        if self.is_empty():
            raise Exception("Deque is empty.")
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Exception("Deque is empty.")
        return self._trailer._prev.element

    
    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next ) # add after header
    
    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """Remove and return the element from the front of the deque.
        Raise Empty exception if the deque is empty."""

        if self.is_empty():
            raise Exception("Deque is empty")
        return self._delete_node(self._header._next)     

    def delete_last(self):
        """Remove and return the element from the back of the deque.
        Raise Empty exception if the deque is empty."""
        if self.is_empty():
            raise Exception("Deque is empty")
        return self._delete_node(self._trailer._prev) 
    
    def printList(self):
        walk = self._header._next
        print("The List contains: ")
        
        while walk != self._trailer:
            print(walk._element, end=" ")
            walk = walk._next
    
    def __iter__(self):
        """Generate a forward iteratoion of the elements of list."""
        cursor = self._header._next
        while cursor != self._trailer:
            yield cursor._element
            cursor = cursor._next
        









if __name__ == "__main__":

    Q = DoublyLinkedDeque()
    Q.insert_first(5)
    Q.insert_first(6)
    Q.insert_first(7)
    Q.insert_first(8)
    Q.insert_first(9)
    Q.insert_first(4)

    Q.printList()

    



