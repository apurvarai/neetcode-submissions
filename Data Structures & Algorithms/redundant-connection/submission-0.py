class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #detecting nodes in a cycle idea
        n=len(edges)
        adj=[[] for _ in range(n+1)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visit=[False]*(n+1)
        st=-2
        cycle=set()
        def dfs(node,par):
            nonlocal st
            if visit[node]:
                st=node
                return True
            visit[node]=True
            for nbd in adj[node]:
                if nbd==par:
                    continue
                if dfs(nbd,node):
                    if st!=-2:
                        cycle.add(node)
                    if st==node:
                        st=-2
                    return True
            return False
        dfs(1,-1)
        print(cycle)
        for u,v in reversed(edges):
            if u in cycle and v in cycle:
                return [u,v]


        