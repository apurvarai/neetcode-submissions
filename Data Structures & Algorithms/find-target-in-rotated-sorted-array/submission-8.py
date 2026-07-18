class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        def check(target,mid,nums):
            return target-nums[mid]>0
        def bs(arr):
            lo=0
            hi=len(arr)-1
            while lo<=hi:
                mid=lo+(hi-lo)//2
                if arr[mid]==target:
                    return mid
                if check(target,mid,arr):
                    # hi=mid-1
                    lo=mid+1
                else:
                    # lo=mid+1
                    hi=mid-1
            return -1

        #find the index of smallest elt in array
        #once that is found, perform bs in 2 sorted arrays
        #nums[0:pivot-1] and nums[pivot,n-1]
        #or compare target with nums[0]
        #if target>nums[0],search in nums[0:pivot-1]
        #if target<nums[0],search in nums[pivot,n-1]
        # else target==nums[0]
        if n==1:
            return 0 if target==nums[0] else -1
        if nums[0]<nums[n-1]:
            pivot=0
        else:
            lo=0
            hi=n-1
            while lo<=hi:
                mid=lo+(hi-lo)//2
                if check(nums[0],mid,nums):
                    pivot=mid
                    hi=mid-1
                else:
                    lo=mid+1
        if pivot==0:
            ans=bs(nums)
        elif target>nums[0]:
            ans=bs(nums[0:pivot])
          
        elif target<nums[0]:
            ans= bs(nums[pivot:n])
            if ans==-1:
                return -1
            return ans+pivot
        else:
            return 0
        return ans
        