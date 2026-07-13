class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        cnt1,cnt2=0,0
        n1,n2=-1,-1
        res=[]
        for i in nums:
            if i==n1:
                cnt1+=1
            elif i==n2:
                cnt2+=1
            elif cnt1==0:
                n1=i
                cnt1=1
            elif cnt2==0:
                n2=i
                cnt2=1
            else:
                cnt1-=1
                cnt2-=1
        c1,c2=0,0
        for i in nums:
            if i==n1:
                c1+=1
            if i==n2:
                c2+=1
        if c1>n//3:
            res.append(n1)
        if c2>n//3:
            res.append(n2)
        return res

        