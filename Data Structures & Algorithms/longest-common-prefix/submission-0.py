class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        com=""
        maxlen=float('inf')
        for i in strs:
            if len(i)<maxlen:
                maxlen=len(i)
        for i in range(maxlen):
            check=strs[0][i]
            for j in range(1,len(strs)):
                if check!=strs[j][i]:
                    return com
                if j==len(strs)-1:
                    com+=check
        return com
        