# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root is None:
                return 0
            return 1+max(height(root.left),height(root.right))
        def dfs(root):
            if root is None:
                return True,0
            bal=False
            bl,hl=dfs(root.left)
            br,hr=dfs(root.right)
            if abs(hl-hr)<=1:
                bal=True
            return (bal and bl and br),1+max(hl,hr)
        bal,h=dfs(root)
        return bal