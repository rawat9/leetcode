# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
            
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)



# Time Complexity:
#     O(N) -> where N = number of nodes in the tree
# Space Complexity: 
#     O(log(N)) in the best case of completely balanced tree
#     O(N) in the worst case of completely unbalanced tree, to keep a recursion stack.