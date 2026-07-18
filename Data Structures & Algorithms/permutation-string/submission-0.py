class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        i=0
        j=len(s1)-1
        while j<len(s2):
            if sorted(s2[i:j+1])==sorted(s1):
                return True
            i+=1
            j+=1
        return False

        