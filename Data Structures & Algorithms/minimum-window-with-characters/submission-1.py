class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l=0
        r=0
        n=len(s)
        if len(s)<len(t):
            return ""
        freqt,freq,freqs={},{},{}
        for i in t:
            freqt[i]=freqt.get(i,0)+1
        def check(freq):
            for i,val in freqt.items():
                if i not in freq or (i in freq and val>freq[i]):
                    return False
            return True
        for i in s:
            freqs[i]=freqs.get(i,0)+1
        if not check(freqs):
            return ""
        res=s
        flag=0
        while l<n and r<n: 
            while r<n and not check(freq):
                freq[s[r]]=1+freq.get(s[r],0)
                r+=1
            # print(s[r])
            while l<n and check(freq):
                freq[s[l]]=freq.get(s[l],0)-1
                l+=1
            curr=s[l-1:r]
            print(curr)
            if len(res)>len(curr):
                res=curr
                flag=1
        
        return res