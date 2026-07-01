# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res=[]
        q=collections.deque()
        q.append(root)

        while q:
            levelnodes=len(q)
            level=[]
            for i in range(levelnodes):
                node=q.popleft()
                # if node:#why do we need this? can Nullptr be added in queue ever?
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # if level:##needed because None can be there is queue at a level, so it adds [] to the res
            res.append(level.copy())
        return res

        