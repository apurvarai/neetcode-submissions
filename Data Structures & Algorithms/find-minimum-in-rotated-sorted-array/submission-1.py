class Solution:
    def check(self,arr:List[int],x:int)->bool:
        return arr[x]-arr[0]>=0
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        lo=0
        hi=n-1
        ans=0
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if self.check(nums,mid):
                lo=mid+1
            else:
                ans=mid
                hi=mid-1
        return nums[ans]
        