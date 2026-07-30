class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        def dfs(r,c,prev):
            if r<0 or r>=m or c<0 or c>=n or prev>=matrix[r][c]:
                return 0
            return 1+max(dfs(r+1,c,matrix[r][c]),dfs(r-1,c,matrix[r][c]),dfs(r,c+1,matrix[r][c]),dfs(r,c-1,matrix[r][c]))
        res=-1
        for i in range(m):
            for j in range(n):
                l=dfs(i,j,-1)
                res=max(res,l)
        return res
        
        