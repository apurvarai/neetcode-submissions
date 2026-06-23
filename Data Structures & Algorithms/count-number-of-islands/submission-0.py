class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir=[[1,0],[-1,0],[0,1],[0,-1]]
        rows,cols=len(grid),len(grid[0])
        cnt=0
        def dfs(r,c):
            if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c]=='0':
                return
            grid[r][c]='0'
            for dr,dc in dir:
                dfs(r+dr,c+dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1':
                    dfs(r,c)
                    cnt+=1
        return cnt