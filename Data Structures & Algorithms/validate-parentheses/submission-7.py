class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        n=len(s)
        # if n%2:
        #     return False
        mp={'(':')','{':'}','[':']'}
        for i in range(len(s)):
            if s[i] in mp:
                st.append(s[i])
            else:
                if len(st)==0:
                    return False
                else:
                    curr=st.pop()
                    if mp[curr]!=s[i]:
                        return False
        if len(st):
            return False
        return True




        