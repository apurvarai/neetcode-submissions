class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        seen=set(nums)
        ans=1
        for i in nums:
            if i+1 in seen:
                j=i+1
                run=1
                while j in seen:
                    run+=1
                    j+=1
                ans=max(ans,run)
        return ans
        
            
        