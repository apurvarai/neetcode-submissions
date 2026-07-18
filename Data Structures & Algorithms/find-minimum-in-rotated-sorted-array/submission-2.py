class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if nums[0]<nums[n-1]:
            return nums[0]
        def check(mid):
            return nums[0]-nums[mid]>0
        lo=0
        hi=n-1
        # ans=-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if check(mid):
                ans=mid
                hi=mid-1
            else:
                lo=mid+1
        return nums[ans]
        