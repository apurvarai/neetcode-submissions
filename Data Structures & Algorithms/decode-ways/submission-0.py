class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=='0':
            return 0
        n=len(s)
        dp=[0]*n
        dp[0]=1*(s[0]!='0')
        dp[1]=1*(s[1]!='0')+1*(1<=10*int(s[0])+int(s[1])<=26 and s[0]!='0')

        for i in range(2,n):
            dp[i]=dp[i-1]*(s[i]!='0') + dp[i-2]*(1<=10*int(s[i-1])+int(s[i])<=26 and s[i-1]!='0')
        return dp[n-1]
        