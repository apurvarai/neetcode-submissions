class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def check(x):
            return nums[x]-target>=0
        n=len(nums)
        lo=0
        hi=n-1
        ans=-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if nums[mid]==target:
                return mid
            if check(mid):
                ans=mid
                hi=mid-1
            else:
                lo=mid+1
        if ans==-1:
            return -1
        if nums[ans]==target:
            return ans
        else:
            return -1

