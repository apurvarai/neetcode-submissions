class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        visit=set(nums)
        res=0
        for i in nums:
            if i-1 not in visit:
                curr=1
                while i+curr in visit:
                    curr+=1
                res=max(res,curr)
        return res

   
                
        