class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #use kahn's algo and just append the node dequed in the res
        n=numCourses
        edges=prerequisites
        res=[]
        indeg=[0]*n
        fin=0
        adj=[[] for _ in range(n)]
        for u,v in edges: #v->u
            indeg[u]+=1
            adj[v].append(u)
        q=deque()
        for i in range(n):
            if indeg[i]==0:
                q.append(i)
        while q:
            node=q.popleft()
            fin+=1
            res.append(node)
            for i in adj[node]:
                indeg[i]-=1
                if indeg[i]==0:
                    q.append(i)
        return res if fin==n else []