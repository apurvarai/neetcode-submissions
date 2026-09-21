class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        def minidx():
            def c1(x):
                return nums[x]-nums[0]>=0
            ans=-1
            lo=0
            hi=n-1
            while lo<=hi:
                mid=lo+(hi-lo)//2
                if c1(mid):
                    lo=mid+1
                else:
                    ans=mid
                    hi=mid-1
            if ans==-1:
                return 0
            else:
                return ans
        piv=minidx()
        l1,h1,l2,h2=0,piv-1,piv,n-1
        # a1,a2=-1,-1
        while l1<=h1:
            m1=l1+(h1-l1)//2
            if nums[m1]==target:
                return m1
            elif nums[m1]>target:
                h1=m1-1
            else:
                l1=m1+1
        while l2<=h2:
            m2=l2+(h2-l2)//2
            if nums[m2]==target:
                return m2
            elif nums[m2]>target:
                h2=m2-1
            else:
                l2=m2+1

        return -1


        