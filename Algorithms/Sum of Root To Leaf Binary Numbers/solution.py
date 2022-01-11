# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def preOrder(root, curr_number):
            nonlocal root_to_leaf
            if root:
                curr_number = (curr_number << 1) | root.val
                if not (root.left or root.right):
                    root_to_leaf += curr_number
                    
                preOrder(root.left, curr_number)
                preOrder(root.right, curr_number) 
        
        root_to_leaf = 0
        preOrder(root, 0)
        return root_to_leaf
