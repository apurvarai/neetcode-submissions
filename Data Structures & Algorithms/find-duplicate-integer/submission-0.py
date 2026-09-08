class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lo=1
        n=len(nums)
        hi=n-1
        while lo<hi:
            mid=lo+(hi-lo)//2
            cnt=len([i for i in nums if i<=mid])
            if cnt>mid:
                hi=mid
            else:
                lo=mid+1
        return lo

        