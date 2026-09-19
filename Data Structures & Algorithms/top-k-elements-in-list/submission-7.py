class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        heap,res=[],[]
        for k1,v in freq.items():
            heapq.heappush(heap,(-v,k1))
        # print(heap)
        while k:
            i,j=heapq.heappop(heap)
            res.append(j)
            k-=1
        # print(heap)
        return res