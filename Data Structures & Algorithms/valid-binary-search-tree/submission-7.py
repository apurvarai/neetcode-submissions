# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res=True
        def dfs(root,lower,upper):
            nonlocal res
            # print(root.val)
            if not root:
                return
            if lower>=root.val or root.val>=upper:
                res=False
                return
            # print(root.val)
            dfs(root.left,lower,root.val)
            dfs(root.right,root.val,upper)
        dfs(root,-float('inf'),float('inf'))
        return res 

        