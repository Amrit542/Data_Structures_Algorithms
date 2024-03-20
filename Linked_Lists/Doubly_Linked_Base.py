class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation"""

    class _Node:
        
        __slots__ = "_element", "_prev", "_next"

        def __init__(self, element, prev, next) -> None:
            self._element = element
            self._prev = prev
            self._next = next
    
    ########################
    def __init__(self) -> None:
        """Create an empty List"""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def _insert_between(self, e, predecessor, successor):
        new_node = self._Node(e, predecessor, successor )
        predecessor._next = new_node
        successor._prev = new_node
        self._size += 1
        return new_node
    
    def _delete_node(self, node: _Node):
        """Delete nonsentinel node from the list and return its element.
            Sentinel = header, trailer
        """
        predecessor =  node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element  # record deleted element
        node._prev = node._next = node._element = None # deprecate node for garbage collection
        return element



    
