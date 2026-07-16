class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        row=len(grid)
        col=len(grid[0])
        visit=[[0]*col for _ in range(row)]
        # res=[[1e8]*col for _ in range(row)]
        dist=-1
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    visit[i][j]=1
                    q.append((i,j))
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                # grid[r][c]=dist
                if r+1>=0 and r+1<row and c>=0 and c<col and grid[r+1][c]==1:
                    q.append((r+1,c))
                    grid[r+1][c]=2
                if r>=0 and r<row and c+1>=0 and c+1<col and grid[r][c+1]==1:
                    q.append((r,c+1))
                    grid[r][c+1]=2
                if r-1>=0 and r-1<row and c>=0 and c<col and grid[r-1][c]==1:
                    q.append((r-1,c))
                    grid[r-1][c]=2
                if r>=0 and r<row and c-1>=0 and c-1<col and grid[r][c-1]==1:
                    q.append((r,c-1))
                    grid[r][c-1]=2
            dist+=1
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    return -1
        return max(0,dist)
        