class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(n+1):
            s=bin(i)[2:]
            curr=0
            for j in range(len(s)):
                rep=int(s)
                mask=(1<<j)
                if (mask&rep):
                    curr+=1
            res.append(curr)

        return res
        