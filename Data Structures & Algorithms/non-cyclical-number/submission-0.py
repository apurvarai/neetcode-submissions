class Solution:
    def isHappy(self, n: int) -> bool:
        def rep(temp):
            # temp=n
            ans=0
            while temp:
                ans+=(temp%10)*(temp%10)
                temp=temp//10
            return ans
        mapp={1:True,2:False,3:False,4:False,5:False,6:False,7:True,8:False,9:False,10:True}
        # while 1:
        if n in mapp:
            return mapp[n]
        else:
            print(rep(n))
            return self.isHappy(rep(n))
            


        