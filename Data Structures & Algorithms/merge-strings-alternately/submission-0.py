class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        n1=len(word1)
        n2=len(word2)
        s=""
        while i<n1 and j<n2:
            s+=word1[i]
            s+=word2[j]
            i+=1
            j+=1
        while i<n1:
            s+=word1[i]
            i+=1
        while j<n2:
            s+=word2[j]
            j+=1
        return s


        