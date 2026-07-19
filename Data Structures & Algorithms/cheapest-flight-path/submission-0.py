class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj=[[] for _ in range(n)]
        for u,v,w in flights:
            adj[u].append([v,w])
        dist=[[float("inf")]*(k+2) for _ in range(n)]
        dist[src][0]=0
        minh=[(0,src,0)]#cost,node,flights_taken
        while minh:
            cost,node,flight=heapq.heappop(minh)
            if node==dst:
                return cost
            if flight==k+1:
                continue
            if cost>dist[node][flight]:
                continue
            for nbd,price in adj[node]:
                newcst=price+cost
                newflight=1+flight
                if dist[nbd][newflight]>newcst:
                    dist[nbd][newflight]=newcst
                    heapq.heappush(minh,[newcst,nbd,newflight])
        return -1
                
        