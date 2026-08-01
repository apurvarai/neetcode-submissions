class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m=len(s1)
        n=len(s2)
        dp=[[False for _ in range(n+1)] for _ in range(m+1)]
        dp[m][n]=True
        for i in range(m+1):
            if s1[i:]==s3[i+n:]:
                dp[i][n]=True
        for j in range(n+1):
            if s2[j:]==s3[j+m:]:
                dp[m][j]=True
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if s1[i]==s3[i+j] and dp[i+1][j]:
                    dp[i][j]=True
                if s2[j]==s3[i+j] and dp[i][j+1]:
                    dp[i][j]=True
        return dp[0][0]