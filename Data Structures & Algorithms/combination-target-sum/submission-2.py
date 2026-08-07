class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=set()
        n=len(nums)
        def dfs(i,curr):
            if i==n and sum(curr)==target:
                res.add(tuple(curr.copy()))
                return
            if i==n or sum(curr)>target:
                return
            curr.append(nums[i])
            # sum+=nums[i]
            dfs(i,curr)
            curr.pop()
            # sum-=nums[i]
            dfs(i+1,curr)
        dfs(0,[])
        result=[]
        for i in res:
            result.append(list(i))
        return result
        