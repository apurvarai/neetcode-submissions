# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def maxd(root):
            if not root:
                return 0
            return 1+max(maxd(root.left),maxd(root.right))
        #for every node
        # 2+maxd(node.left)+maxd(node.right)
        ans=maxd(root.left)+maxd(root.right)
        # ans=max(ans,)
        return max(ans,self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))


        