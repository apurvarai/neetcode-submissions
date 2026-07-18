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
        def check(root):
            if root is None:
                return -10000
            return max(root.val,check(root.left),check(root.right))
        def check2(root):
            if root is None:
                return 10000
            return min(root.val,check2(root.left),check2(root.right))
        return self.isValidBST(root.left) and self.isValidBST(root.right) and root.val<check2(root.right) and check(root.left)<root.val
        