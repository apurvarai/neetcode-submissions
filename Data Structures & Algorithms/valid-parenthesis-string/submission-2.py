class Solution:
    def checkValidString(self, s: str) -> bool:
        n=len(s)
        ans=False
        def isvalid(st):
            stack=[]
            for i in range(len(st)):
                if st[i]=='(':
                    stack.append(st[i])
                else:
                    if len(stack)==0:
                        return False
                    stack.pop()
            if len(stack):
                return False
            return True
        def dfs(i,curr):
            nonlocal ans
            if ans:
                return
            if i==n:
                # print(curr,isvalid(curr))
                if isvalid(curr):
                    ans=True
                return
            if s[i]=='(' or s[i]==')':
                dfs(i+1,curr+s[i])
            else:
                dfs(i+1,curr+'(')
                dfs(i+1,curr+')')
                dfs(i+1,curr)
        # ans=False
        dfs(0,"")
        return ans

        