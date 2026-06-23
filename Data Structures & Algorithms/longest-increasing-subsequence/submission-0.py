class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*n
        dp[n-1]=1
        lastnum=nums[n-1]

        for i in range(n-2,-1,-1):
            if nums[i]<lastnum:
                dp[i]=dp[i+1]+1
                lastnum=nums[i]
            else:
                dp[i]=dp[i+1]
        return dp[0]

        