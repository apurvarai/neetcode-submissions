class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        res=[]
        if all(x==9 for x in digits):
            res.append(1)
            for j in range(n):
                res.append(0)
            return res

        
        if digits[n-1]==9:
            last=n-1
            for j in range(n-2,0,-1):
                if digits[j]==9:
                    last=j
                else:
                    break
            cnt=0
            while cnt<last:
                res.append(digits[cnt])
                cnt+=1
            res.append(digits[cnt]+1)
            while cnt<len(digits):
                res.append(0)
                cnt+=1

        else:
            i=0
            while i<n-1:
                res.append(digits[i])
                i+=1
            res.append(digits[n-1]+1)
        return res