# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root):
            if not root:
                return []
            res = [root.val] + dfs(root.left) + dfs(root.right)
            return list(filter(lambda x: x <= high and x >= low, res))
        
        return sum(dfs(root))