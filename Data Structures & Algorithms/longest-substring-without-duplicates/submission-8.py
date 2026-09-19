class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp={}
        i,j=0,0
        res=0
        n=len(s)
        if n==0:
            return 0
        while j<n:
            if s[j] in mp and mp[s[j]]>=i:
                i=mp[s[j]]+1
            mp[s[j]]=j
            res=max(res,j-i+1)
            j+=1
        return res


        