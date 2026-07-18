class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        i=0
        j=len(s1)-1
        f1=collections.Counter(s1)
        f2=collections.Counter(s2[i:j])
        while j<len(s2):
            f2[s2[j]]=1+f2.get(s2[j],0)
            if f1==f2:
                return True
            f2[s2[i]]=f2.get(s2[i],0)-1
            # f2[s2[j+1]]=f2.get(s2[j+1],0)+1
            i+=1
            j+=1
        return False

        