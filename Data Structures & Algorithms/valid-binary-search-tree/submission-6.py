# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res=True
        def dfs(root):
            nonlocal res
            # print(root.val)
            if not root:
                return
            if (root.left and root.left.val>=root.val) or (root.right and root.val>=root.right.val):
                res=False
                return
            # print(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res 

        