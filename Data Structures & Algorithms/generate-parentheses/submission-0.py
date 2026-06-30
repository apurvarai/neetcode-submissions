class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def valid(s):
            score=0
            for j in range(len(s)):
                if s[j]=='(':
                    score+=1
                else:
                    score-=1
                if score<0:
                    return False
                if j==len(s)-1 and score!=0:
                    return False
            return True
        def dfs(curr):
            if len(curr)==2*n:
                if valid(curr):
                    res.append(curr)
                return
            # curr+="("
            # dfs(curr)
            # curr
            dfs(curr+'(')
            dfs(curr+')')
        dfs("")
        return res