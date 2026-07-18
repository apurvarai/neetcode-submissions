# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def dfs(root):
            if not root:
                return [True,0]
            a,b=dfs(root.left)
            c,d=dfs(root.right)
            return [a and c and (abs(b-d)<=1),1+max(b,d)]
        a,b= dfs(root)
        return a
        
        