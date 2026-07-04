# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def getmax(root):
            if not root:
                return 0
            path=root.val+max(getmax(root.left),getmax(root.right))
            return path
        res=-float('inf')
        # if not root:
        #     return
        def dfs(root):
            nonlocal res
            if not root:
                return
            left=getmax(root.left)
            right=getmax(root.right)
            res=max(res,root.val+left+right)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res
            
        