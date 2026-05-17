import math
class Solution:
    def check(self,x:int,piles:List[int],h:int)->bool:
        sum=0
        for i in piles:
            sum+=math.ceil(i/x)
        if sum<=h:
            return True
        return False
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles)==h:
            return max(piles)
        ##we have a range of k [sum(piles)/h , max(piles)]
        ##we apply a bs in this range and see if x is a solution
        #if x is a sol we store ans=x and hi=x-1
        #else we do lo=x+1
        #to find if x is a sol
        #we divide each elt of pile by x and take ceil of it and sum it up
        #if the sum we get is <=h, x is a sol
        lo=math.ceil(sum(piles)/h)
        hi=max(piles)
        ans=max(piles)
        while(lo<=hi):
            x=lo+(hi-lo)//2
            if self.check(x,piles,h):
                ans=x
                hi=x-1
            else:
                lo=x+1
        return ans

        