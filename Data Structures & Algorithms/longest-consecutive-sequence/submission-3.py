class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        ans=0
        curr=1
        nums.sort()
        prev=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==prev+1:
                curr+=1
                prev=nums[i]
            elif nums[i]==prev:
                continue
            else:
                ans=max(ans,curr)
                curr=1
                prev=nums[i]
        # for i in nums:
        ans=max(ans,curr)
        return ans
        #     prev=i
        #     len=1
        #     if i==prev+1:
        #         prev=j
        #         len+=1
        #     ans=max(len,ans)
        return ans
                
        