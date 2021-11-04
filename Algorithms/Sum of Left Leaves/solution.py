# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        # if there's no root present
        if not root:
            return 0
        
        # check if there's left child that is a leaf node
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        
        # if there's no left child or left node doesn't exists
        else:
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
