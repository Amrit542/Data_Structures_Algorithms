class BinaryTree:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None) -> None:
            self.val = val
            self.left = left
            self.right = right
    
    def __init__(self) -> None:
        self.root = None
        self.size = 0
        
    def __len__(self):
        return self.size
    
    def insert(self, val=None):
        node = self.TreeNode(self, val)

        curr = self.root
        