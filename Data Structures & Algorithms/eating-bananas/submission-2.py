class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo=math.ceil(sum(piles)/h)
        hi=max(piles)
        nums=piles
        def check(mid):
            sum=0
            for i in piles:
                sum+=math.ceil(i/mid)
            if sum<=h:
                return True
            return False
            # return sum(nums)//mid<=h
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if check(mid):
                ans=mid
                hi=mid-1
            else:
                lo=mid+1
        return ans

        