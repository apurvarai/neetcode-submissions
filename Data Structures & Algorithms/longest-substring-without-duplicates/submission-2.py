class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visit=set()
        n=len(s)
        i=0
        j=0
        ans=0
        while j<n:
            if s[j] in visit:
                while s[j] in visit and i<=j:
                    visit.remove(s[i])
                    i+=1
                visit.add(s[j])
            else:
                visit.add(s[j])
            ans=max(ans,j-i+1)
            j+=1
            
            print(visit,ans,s[i:j+1])

        return ans
        