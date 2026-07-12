class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #find the first right elt from right, which is lesser than it's right elt
        #find the next greater elt than the above elt in right of it
        #then since right of pivot, are in desecending, we reverese pivot+1 till end array
        n=len(nums)
        i=n-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        if i>=0:
            j=n-1
            while j>=0 and nums[j]<=nums[i]:
                j-=1
            nums[j],nums[i]=nums[i],nums[j]
        nums[i+1:]=nums[i+1:][::-1]

        