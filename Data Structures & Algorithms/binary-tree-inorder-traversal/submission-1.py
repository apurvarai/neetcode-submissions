# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # res=[]
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # res=[]
        if root is None:
            return []
        # if root.left is None and root.right is None:
        #     res.append(root.val)
        #     return
        l=self.inorderTraversal(root.left)
        # res.append(root.val)
        r=self.inorderTraversal(root.right)
        return l+[root.val]+r
        # def dfs(root):
        #     if root is None:
        #         return [] 
            # dfs(root.left)
            # res.append(root.val)
            # dfs(root.right)



        # dfs(root)   
        # return res

        