class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        for i in range(n-2,-1,-1):
            if nums[i]>=n-1-i:
                return True
        
        return False
        