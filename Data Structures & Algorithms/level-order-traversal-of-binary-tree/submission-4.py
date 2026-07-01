# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        q=collections.deque()
        q.append(root)

        while q:
            levelnodes=len(q)
            level=[]
            for i in range(levelnodes):
                node=q.popleft()
                if node:#why do we need this? can Nullptr be added in queue ever?
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level.copy())
        return res

        