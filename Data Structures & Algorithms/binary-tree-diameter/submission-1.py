# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=0
        if root is None:
            return 0
        def maxd(root):
            if root is None:
                return 0
            return 1+max(maxd(root.left),maxd(root.right))
        diameter=maxd(root.left)+maxd(root.right)
        return max(ans,maxd(root.left)+maxd(root.right))
        