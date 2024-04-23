class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def deleteNode(self, root, key):
        if root is None:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            successor = self.minValueNode(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)
        return root
    
    def minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current