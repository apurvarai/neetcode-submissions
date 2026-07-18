class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans=0
        nums.sort()
        for i in nums:
            prev=i
            len=1
            for j in nums:
                if j==prev+1:
                    prev=j
                    len+=1
            ans=max(len,ans)
        return ans
                
        