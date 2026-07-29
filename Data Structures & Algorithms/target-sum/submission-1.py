class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        S=sum(nums)
        dp=[[0 for _ in range(2*S+1)] for _ in range(n+1)]
        for i in range(2*S+1):
            dp[n][i]=1 if i==target+S else 0
        for i in range(n-1,-1,-1):
            for a in range(2*S+1):
                dp[i][a]=(dp[i+1][a-nums[i]] if a>=nums[i] else 0)+(dp[i+1][a+nums[i]] if a+nums[i]<=2*S else 0)
        return dp[0][S]

        