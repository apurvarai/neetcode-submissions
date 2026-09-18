class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix,suffix,out=[0 for _ in range(n)],[0 for _ in range(n)],[0 for _ in range(n)]
        n=len(nums)
        prefix[0]=nums[0]
        suffix[n-1]=nums[n-1]
        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i]
        for i in range(n-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i]
        out[0],out[n-1]=suffix[1],prefix[n-2]
        for i in range(1,n-1):
            out[i]=prefix[i-1]*suffix[i+1]
        return out
        