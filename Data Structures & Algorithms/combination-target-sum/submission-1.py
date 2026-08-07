class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=set()
        n=len(nums)
        def dfs(i,curr,sum):
            if i==n and sum==target:
                res.add(tuple(curr.copy()))
                return
            if i==n or sum>target:
                return
            curr.append(nums[i])
            sum+=nums[i]
            dfs(i,curr,sum)
            curr.pop()
            sum-=nums[i]
            dfs(i+1,curr,sum)
        dfs(0,[],0)
        result=[]
        for i in res:
            result.append(list(i))
        return result
        