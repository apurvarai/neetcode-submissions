# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
            # root.val=val
            # root.left=None
            # root.right=None
        if root.val<val:
            #insert into right subtree
            root.right=self.insertIntoBST(root.right,val)
        else:
            #insert into left subtree
            root.left=self.insertIntoBST(root.left,val)
        return root

        