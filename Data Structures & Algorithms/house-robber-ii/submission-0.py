class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        
        if n==1:
            return nums[0]
        return max(self.help(nums[1:]),self.help(nums[:-1]))
        
    def help(self,nums:List[int]) -> int:
            n=len(nums)
            if n==1:
                return nums[0]
            dp=[-1]*(n+1)
            dp[n]=0
            dp[n-1]=nums[n-1]
            for i in range(n-2,-1,-1):
                dp[i]=max(dp[i+1],dp[i+2]+nums[i])
            return dp[0]
            # if i>=n:
            #     return 0
            # if dp[i]!=-1:
            #     return dp[i]
            # dp[i]=max(rec(i+1),nums[i]+rec(i+2))
            # return dp[i]
        
        # return max(rob(nums[1:]),rob(nums[:-1]))