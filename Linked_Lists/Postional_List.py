from Doubly_Linked_Base import _DoublyLinkedBase

class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

    # ---------------Nested Positon class --------------
    class Postion:
        "An abstraction representing the location of a single element."
        
        def __init__(self, container, node) -> None:
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node
        
        def element(self):
            """Return the element stored at this position."""
            self._node._element
        
        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node
        
        def __ne__(self, other):
            """Return True if other does not represent the same location"""
            return not (self == other)
        
    # ----------------Utility Method ----------------------------
        
    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Postion):
            raise TypeError("p must be proper Position type.")
        if p._container is not self :
            raise ValueError("p does not belong to this container")
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node or None if it is sentinel."""
        if node is self._header or node is self._trailer:
            return None                # Boundary violation
        else:
            return self.Postion(self, node)   # legitimate position
    
    # ----------------------Accessors -------------------------------
    
    def first(self):
        """Return the first position in the list or None if list is empty."""
        if self.is_empty():
            return None
        return self._make_position(self._header._next)
    
    def last(self):
        """Return the last position in the list or None if list is empty."""
        if self.is_empty():
            return None
        return self._make_position(self._trailer._prev)



    def before(self, p):
        """Return the position just before Positon p (or None if p is first)."""
        node = self._validate(p)
        return self._make_position(node._prev)
    
    def after(self, p):
        """Return the position just after Positon p (or None if p is last)."""
        node = self._validate(p)
        return self._make_position(node._next)
    
    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
    
    # ------------------Mutators---------------------------------
    
    # Override inherited version to return positon, rather than Node
    def _insert_between(self, e, predecessor, successor):
        node =  super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """Insert element e at the front of the list and return new Position."""
        return self._insert_between(e, self._header, self._header._next)
    
    def add_last(self, e):
        """Insert element e at the back of the list and return new Position."""
        return self._insert_between(e, self._trailer._prev, self._trailer)
    
    def add_before(self, p, e):
        """Insert element e into the list before positon p and return new Position."""
        original = self._validate(p)     # return node at position p
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """Insert element e into the list after positon p and return new Position."""
        original = self._validate(p)     # return node at position p
        return self._insert_between(e, original, original._next)
    
    def delete(self, p):
        """Remove and return the element at Position p"""
        original = self._validate(p) 
        return self._delete_node(original)   # Inherited method returns element
    
    def replace(self, p, e):
        """Replace the element at Position p with e.
        Return the element formerly at Position p.        
        """
        original = self._validate(p)
        old_value = original._element
        original._element = e  # replace with new element
        return old_value       # return the old element value
 




def sort(L: PositionalList ):
    val = L.first().element
    print(val)

if __name__ == "__main__":

    L = PositionalList()
    L.insert_first(5)
    L.insert_first(7)
    L.insert_first(8)
    L.insert_first(6)
    L.insert_first(9)
    L.insert_first(4)

    L.printList()
