class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums=candidates
        n=len(nums)
        res=set()
        def dfs(i,curr,s):
            if i==n and s==target:
                res.add(tuple(curr.copy()))
                return
            if i==n or s>target:
                return
            s+=nums[i]
            curr.append(nums[i])
            dfs(i+1,curr,s)
            s-=nums[i]
            curr.pop()
            dfs(i+1,curr,s)
        dfs(0,[],0)
        result=[]
        for i in res:
            result.append(list(i))
        return result
        