# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:           

	# perform inOrder traversal 
	# check whether the temp list is sorted -> True else False
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        temp = []
        def dfs(node=root):
            if node:
                dfs(node.left)
                temp.append(node.val)
                dfs(node.right)
        dfs()
        first = temp[0]
        
        for i in range(1, len(temp)):
            if first >= temp[i]:
                return False
            first = temp[i]
        return True        
