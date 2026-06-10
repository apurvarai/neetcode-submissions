class Solution:
    def rob(self, nums: List[int]) -> int:
        odd=0
        even=0
        n=len(nums)
        for i in range(0,n,2):
            odd+=nums[i]
        for i in range(1,n,2):
            even+=nums[i]
        return max(odd,even)

        