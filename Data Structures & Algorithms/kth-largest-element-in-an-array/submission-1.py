class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n=len(nums)
        heapq.heapify(nums)
        j=n-k
        while j:
            heapq.heappop(nums)
            # print(nums)
            j-=1
        return nums[0]
        