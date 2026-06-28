class Solution:
    def validPalindrome(self, s: str) -> bool:
        def ispalindrome(s):
            i=0
            j=len(s)-1
            while i<j:
                if s[i]==s[j]:
                    i+=1
                    j-=1
                else:
                    return False
            return True
        if(ispalindrome(s)):
            return True
        for i in range(len(s)):
            if(ispalindrome(s[:i]+s[i+1:])):
                return True
        return False
        