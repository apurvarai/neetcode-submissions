class Solution:
    def check(self, lst:List[int],x:int,target:int)->bool:
        return lst[x]-target>=0

    def search(self, nums: List[int], target: int) -> int:
        ##we need to first find min_idx
        #then we separate list as [0,minidx-1] and [minidx,n-1]
        #we apply bs to both these lst and find the first 1
        #exactly one of them will return true, if not return -1

        #finding minidx
        n=len(nums)
        lo=0
        hi=n-1
        ans=n
        while(lo<=hi):
            mid=lo+(hi-lo)//2
            if self.check(nums,mid,nums[0]):
                lo=mid+1
            else:
                ans=mid
                hi=mid-1
        ##ans here stores minidx

        # lst=nums[0:ans]
        # lst2=nums[ans:n]
        # lo1=0
        # hi1=ans-1
        ans1=-1
        if (target>=nums[0]):
            # lst1=lst2
            lo1=0
            hi1=ans-1
        else:
            # lst1=lst
            lo1=ans
            hi1=n-1

        while(lo1<=hi1):
            mid1=lo1+(hi1-lo1)//2
            if nums[mid1]==target:
                return mid1
            if self.check(nums,mid1,target):
                ans1=mid1
                hi1=mid1-1
            else:
                # ans1=mid1
                lo1=mid1+1
        if nums[ans1]==target: 
            return ans1
        else:
            return -1
        # return ans1
