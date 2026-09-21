class Solution:
    def findMin(self, nums: List[int]) -> int:
        def check(x):
            return nums[x]-nums[0]>=0
        n=len(nums)
        ans=-1
        lo=0
        hi=n-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if check(mid):
                lo=mid+1
            else:
                ans=mid
                hi=mid-1
        if ans==-1:
            return nums[0]
        else:
            return nums[ans]
        