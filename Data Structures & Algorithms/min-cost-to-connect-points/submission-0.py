class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parent=[i for i in range(len(points))]

        def find(x):
            if x!=parent[x]:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            px,py=find(x),find(y)
            if px==py:
                return False
            parent[py]=px
            return True


        # adj=collections.defaultdict(list)
        adj=[]
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                x,y=points[i]
                p,q=points[j]
                adj.append(((abs(x-p)+abs(y-q)),i,j))
        adj.sort()
        res=0
        for dist,u,v in adj:
            if union(u,v):
                res+=dist
        return res
        
        # for x,y in points:
        #     for x1,y1 in points:
        #         adj[(x,y)].append((x1,y1),(abs(x-x1)+abs(y-y1)))
        