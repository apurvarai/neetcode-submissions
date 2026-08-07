class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums=candidates
        n=len(nums)
        res=set()
        def dfs(i,curr):
            if i==n and sum(curr)==target:
                res.add(tuple(curr.copy()))
                return
            if i==n or sum(curr)>target:
                return
            curr.append(nums[i])
            dfs(i+1,curr)
            curr.pop()
            dfs(i+1,curr)
        dfs(0,[])
        result=[]
        for i in res:
            result.append(list(i))
        return result
        