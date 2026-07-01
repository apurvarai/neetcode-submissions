class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        part=[]
        def ispal(s1):
            return s1==s1[::-1]
        def dfs(i,st,curr):
                if i>=len(s):
                    print(curr)
                    res.append(curr.copy())
                    return
                if ispal(st):
                    print(st)
                    curr.append(st)
                print(i)
                st+=s[i]
                dfs(i+1,st,curr)
                curr.pop()
                dfs(i+1,"",curr)
        dfs(0,"",[])
        return res

        