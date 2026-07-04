class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        dist=[]
        for i in range(len(points)):
            print(points[i][1])
            dist.append(((points[i][0])**2+(points[i][1])**2)**.5)
            res.append((dist[i],points[i]))
        heapq.heapify(res)

        result=[]
        while k:
            result.append(res[0][1])
            print(res[0][1])
            heapq.heappop(res)
            k-=1
        return result

        