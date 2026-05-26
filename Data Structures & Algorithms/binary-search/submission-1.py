class Solution:

    def check(self,x:int,nums:List[int],target:int)->bool:
        return (nums[x]-target)>=0
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        lo=0
        hi=n-1
        ans=nums[0]
        while lo<hi:
            mid=lo+(hi-lo)//2
            if nums[mid]==target:
                return mid
            else:
                if self.check(mid,nums,target)==1:
                    hi=mid
                    ans=mid
                else:
                    lo=mid+1
        if nums[ans]==target:
            return ans
        else:
            return -1
        