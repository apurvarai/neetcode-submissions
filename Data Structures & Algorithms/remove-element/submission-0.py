class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        cnt=0
        i=0
        while i<len(nums):
            # print(i)
            if nums[i]==val:
                nums.remove(nums[i])
                # i-=1
                cnt+=1
            else:
                i+=1
        return n-cnt
        