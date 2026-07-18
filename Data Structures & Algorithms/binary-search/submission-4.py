class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        lo=0
        hi=n-1
        ans=-1
        def check(mid):
            return target-nums[mid]>=0
        while lo<=hi:
            mid=lo+(hi-lo)//2
            print(mid)
            if nums[mid]==target:
                return mid
            if check(mid):
                # ans=mid
                lo=mid+1
            else:
                hi=mid-1
        return ans