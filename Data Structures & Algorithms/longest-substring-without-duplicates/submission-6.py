class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        n=len(s)
        visit=set()
        res=0
        while j<n:
            while s[j] in visit:
                visit.remove(s[i])
                i+=1
            visit.add(s[j])
            j+=1
            res=max(res,len(visit))
        return res




 
        