class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j=0,0
        seen=set()
        ans,run=0,0
        n=len(s)
        if n==0:
            return 0
        while j<n:
            if s[j] not in seen:
                seen.add(s[j])
                j+=1
            else:
                while s[j] in seen:
                    seen.remove(s[i])
                    i+=1
                seen.add(s[j])
                j+=1
            run=j-i
            ans=max(ans,run)
        return ans
