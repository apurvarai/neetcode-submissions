class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        part=[]
        def ispal(s,i,j):
            # return s1==s1[::-1]
            s1=s[i:j+1]
            return s1==s1[::-1]
        print(ispal("ababa",0,2))
        def dfs(i):
            if i>=len(s):
                res.append(part.copy())
                return
            for j in range(i,len(s)):
                if ispal(s,i,j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res
        # def dfs(i,st,curr):
        #         if i>=len(s):
        #             print(curr)
        #             res.append(curr.copy())
        #             return
        #         if ispal(st):
        #             print(st)
        #             curr.append(st)
        #         print(i)
        #         st+=s[i]
        #         dfs(i+1,st,curr)
        #         curr.pop()
        #         dfs(i+1,"",curr)
        # dfs(0,"",[])
        # return res

        