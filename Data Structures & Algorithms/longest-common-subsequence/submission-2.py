class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1=len(text1)
        l2=len(text2)
        t1=text1
        t2=text2
        dp=[[0]*l2 for _ in range(l1)] #dp=l1*l2
        dp[0][0]=1 if t1[0]==t2[0] else 0
        for i in range(1,l1):
            if t1[i]==t2[0]:
                dp[i][0]=1
            dp[i][0]=max(dp[i][0],dp[i-1][0])
        for i in range(1,l2):
            if t2[i]==t1[0]:
                dp[0][i]=1
            dp[0][i]=max(dp[0][i],dp[0][i-1])
        for i in range(1,l1):
            for j in range(1,l2):
                if t1[i]==t2[j]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])

                # dp[i][j]=max(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+(1 if t1[i]==t2[j] else 0)
        print(dp)
        return dp[l1-1][l2-1]
        