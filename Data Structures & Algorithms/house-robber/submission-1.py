class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1]*n

        def rec(i):
            if i>=n:
                return 0
            if dp[i]!=-1:
                return dp[i]
            dp[i]=max(rec(i+1),nums[i]+rec(i+2))
            return dp[i]
        return rec(0)


        