class Solution:
    def check(self,arr:List[int],days:int,w:int)->bool:
        n=len(arr)
        curr=0
        days-=1
        for i in range(n):
            if curr+arr[i]<=w:
                curr+=arr[i]
            else:
                days-=1
                curr=arr[i]
        # print(days,w)
        if days>=0:
            return True
        return False


    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lo=max(weights)
        hi=sum(weights)
        ans=sum(weights)
        n=len(weights)
        while(lo<=hi):
            mid=lo+(hi-lo)//2
            if self.check(weights,days,mid):
                ans=mid
                hi=mid-1
            else:
                lo=mid+1
        return ans

        
        