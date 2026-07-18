class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        visit=set(s)
        res=0
        for c in visit:
            l=0
            cnt=0
            for r in range(len(s)):
                if s[r]==c:
                    cnt+=1
                while (r-l+1)-cnt>k:
                    if s[l]==c:
                        cnt-=1
                    l+=1
                res=max(res,r-l+1)
        return res

        