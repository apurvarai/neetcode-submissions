# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def dfs(root,minv,maxv):
            if root is None:
                return True
            
            return minv<root.val and root.val<maxv and dfs(root.left,minv,root.val) and dfs(root.right,root.val,maxv)
        return dfs(root,float('-inf'),float('inf'))
        # if root.left is None and root.right is None:
        #     return True
        # if root.left is None:
        #     return root.val<root.right.val
        # if root.right is None:
        #     return root.val>root.left.val
        # return root.left.val<root.val and root.right.val>root.val and self.isValidBST(root.left) and self.isValidBST(root.right) 
        