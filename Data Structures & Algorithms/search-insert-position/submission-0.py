class Solution:
    def check(self,nums:List[int],mid:int,target:int)->bool:
        return nums[mid]-target>=0
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        lo=0
        hi=n-1
        ans=n
        while(lo<=hi):
            mid=lo+(hi-lo)//2
            if nums[mid]==target:
                return mid
            if self.check(nums,mid,target):
                ans=mid
                hi=mid-1
            else:
                lo=mid+1
        return ans