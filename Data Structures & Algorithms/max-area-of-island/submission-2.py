class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #cnt that in a given dfs how many cells are included
        #maintain a list for each dfs,store in in set as a tuple
        #for each dfs, we store it's call in the list, when new dfs starts we store this list as a tuple in the set
        #count the max len of such length after all dfs done
        # visit=set()
        # curr=[]
        m,n=len(grid),len(grid[0])
        def dfs(r,c):
            if r<0 or r>=m or c<0 or c>=n or grid[r][c]==0:
                return 0
            curr.append([r,c])
            grid[r][c]=0
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            return len(curr)
        res=0
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    curr=[]
                    
                    res=max(res,dfs(r,c))
        return res

        