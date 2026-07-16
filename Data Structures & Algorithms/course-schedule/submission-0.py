class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #kahn's algorithm(bfs topological sorting)
        edges=prerequisites
        n=numCourses
        indeg=[0]*n
        finish=0
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[v].append(u)
            indeg[u]+=1
        q=deque()
        for i in range(n):
            if indeg[i]==0:
                q.append(i)
        while q:
            node=q.popleft()
            finish+=1
            for nbd in adj[node]:
                indeg[nbd]-=1
                if indeg[nbd]==0:
                    q.append(nbd)
        return finish==n
            

        