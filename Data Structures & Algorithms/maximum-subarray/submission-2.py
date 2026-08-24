class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # curr=0
        prefix=0
        min_p=0
        res=-float('inf')
        for x in nums:
            prefix+=x
            res=max(res,prefix-min_p)
            min_p=min(min_p,prefix)
        return res