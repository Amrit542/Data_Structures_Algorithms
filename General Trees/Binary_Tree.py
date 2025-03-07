from Tree_Base import Tree
from collections import deque 

class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""

    # ------- Additional abstract methods ---------------
    def left(self, p):
        """Return a Position representing p's left child.

        Return None if p does not have a left child.        
        """
        raise NotImplementedError("Must be implemented by subclass")
    
    def right(self, p):
        """Return a Position representing p's right child.

        Return None if p does not have a right child.        
        """
        raise NotImplementedError("Must be implemented by subclass")

    # ------- Concrete Methods implemented in this class -------------

    def sibling(self, p):
        """Return a Position representing p's sibling or None if no sibling."""
        parent = self.parent(p)
        if parent is None:  # p must be root
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """Generate an iteration of Positions representing p's children."""
        if self.left(p) is not None:
            yield self.left(p)

        if self.right(p) is not None:
            yield self.right(p)

    # Override inherited version to make inorder the default.
    def positions(self): 
        """Generate an iteration of the tree's positions."""
        return self.inorder()   

    def inorder(self):
        """Generate an inorder iteration of Positions in the tree."""
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """Generate a inorder iteration of positions in the subtree rooted at p."""
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p         # Visit p between its subtrees.
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other
