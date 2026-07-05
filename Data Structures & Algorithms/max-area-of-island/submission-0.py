class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res=0
        row=len(grid)
        col=len(grid[0])

        def dfs(r,c):
            nonlocal cnt
            cnt+=1
            grid[r][c]=0
            if r+1>=0 and r+1<row and c>=0 and c<col and grid[r+1][c]:    
                dfs(r+1,c)  
            if r-1>=0 and r-1<row and c>=0 and c<col and grid[r-1][c]: 
                dfs(r-1,c) 
            if r>=0 and r<row and c+1>=0 and c+1<col and grid[r][c+1]:
                dfs(r,c+1) 
            if r>=0 and r<row and c-1>=0 and c-1<col and grid[r][c-1]:
                dfs(r,c-1) 
            return cnt
        for r in range(row):
            for c in range(col):
                if grid[r][c]:
                    cnt=0
                    res=max(res,dfs(r,c))

        return res
        