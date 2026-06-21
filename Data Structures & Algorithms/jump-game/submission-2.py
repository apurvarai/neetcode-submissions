class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n=len(nums)
        if n==1:
            return True
        goal=n-1
        for i in range(n-2,-1,-1):
            if nums[i]>=goal-i:
                goal=i
                # print(i)
        if goal==0:
            return True
        
        return False
        