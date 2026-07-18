class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        freq=collections.Counter(nums)
        print(freq)
        res=[]
        # while k:
        heap=[]
        for i,j in freq.items():
            heapq.heappush(heap,(j,i))
            if len(heap)>k:
                heapq.heappop(heap)
        while k:
            i,j=heapq.heappop(heap)
            res.append(j)
            k-=1
        return res
        # for i,j in freq.items():
        #     res.append(i)
        #     if len(res)==k:
        #         return res
        #build max heap out of freq

        