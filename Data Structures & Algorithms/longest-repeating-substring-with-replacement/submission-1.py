class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        visit=set(s)
        res=0
        temp=k
        for i in visit:
            curr=i
            ans=0
            k=temp
            for j in range(len(s)):
                if s[j]==curr:
                    ans+=1
                elif s[j]!=curr and k>0:
                    k-=1
                    ans+=1
                else:
                    break
            print(curr, ans)
            res=max(res,ans)
        return res