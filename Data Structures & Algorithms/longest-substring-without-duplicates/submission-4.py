class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j=0,0
        visit=set()
        res=0
        while j<len(s):
            if s[j] in visit:
                while s[j] in visit:
                    visit.remove(s[i])
                    i+=1
            visit.add(s[j])
            res=max(res,j-i+1)
            j+=1
        return res
        