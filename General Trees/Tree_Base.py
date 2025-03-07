from collections import deque 

class Tree:
    """Abstract base class representing a tree structure"""

    # ------------------- Nested Positon class ----------------
    class Postion:
        """An abstraction representing the location of a single element."""

        def element(self):
            """Return the element stored at this position."""
            raise NotImplementedError("Must be implemented by subclass")
        
        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError("Must be implemented by subclass")
        
        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)
    
    # ------------ Abstract Methods that concrete subclass must support ---------
    
    def root(self):
        """Return Position representing the tree's root or None if empty."""
        raise NotImplementedError("Must be implemented by subclass")
    
    def parent(self, p):
        """Return Position representing p's parent or None if p is root."""
        raise NotImplementedError("Must be implemented by subclass")
    
    def num_children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError("Must be implemented by subclass")
    
    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        raise NotImplementedError("Must be implemented by subclass")
    
    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError("Must be implemented by subclass")
    
    # --------Concrete methods implemented in this class -------------

    def is_root(self,  p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p
    
    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0
    
    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

    def __iter__(self):
        """Generate an iteration of the tree's elements."""
        for p in self.postions():
            yield p.element()

    def breadthfirst(self):
        """Generate a breadth-first iteration of the positions of the tree."""
        if not self.is_empty():
            queue = deque()
            queue.append(self.root())   # starting with root.
            while queue:
                p = queue.pop()
                yield p            # report this position.
                for c in self.children(p):
                    queue.append(c) # add children back to the queue.

    def preorder(self):
        """Generate a preorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        """Generate a preorder iteration of positions in the subtree rooted at p."""
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    def postorder(self):
        """Generate a postorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        """Generate a postorder iteration of positions in the subtree rooted at p."""
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other
        yield p   

