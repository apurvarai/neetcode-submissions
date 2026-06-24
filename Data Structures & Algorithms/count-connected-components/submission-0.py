class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res=0
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit=[False]*n
        def dfs(node):
            for nbd in adj[node]:
                if not visit[nbd]:
                    visit[nbd]=True
                    dfs(nbd)
        for i in range(n):
            if not visit[i]:
                visit[i]=True
                dfs(i)
                res+=1
        return res

        