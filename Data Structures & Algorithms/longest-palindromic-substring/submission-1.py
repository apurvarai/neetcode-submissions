class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n=len(s)
        if n==1:
            return s
        dp=[[False]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i]==s[j] and (j-i<=2 or dp[i+1][j-1]):
                    dp[i][j]=True
        for l in range(n-1,0,-1):
            for j in range(l,n):
                if dp[j-l][j]:
                    return s[j-l:j+1]
        # for i in range(0,n):
        #     for j in range(0,n):
        #         print(dp[i][j]," ")
        #     print("\n")
        # return s



        