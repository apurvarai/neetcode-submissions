class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # curr=0
        res=-float('inf')
        if len(nums)==1:
            return nums[0]
        pnums=[nums[i] for i in range(len(nums))]
        for i in range(1,len(nums)):
            pnums[i]=pnums[i-1]+nums[i]
        for i in range(len(nums)):
            # curr=0
            for j in range(len(nums)):
                # curr+=pnums[j]-pnums[i-1]
                res=max(res,pnums[j]-pnums[i-1])
        return res
        