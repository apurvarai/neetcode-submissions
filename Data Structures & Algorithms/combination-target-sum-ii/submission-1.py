class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=set()
        n=len(candidates)
        def dfs(i,total,subset):
            if i==n and total==target:
                res.add(tuple(sorted(subset)))
                return
            if i==n or total>target:
                return
            total+=candidates[i]
            subset.append(candidates[i])
            dfs(i+1,total,subset)
            total-=candidates[i]
            subset.pop()
            dfs(i+1,total,subset)
        dfs(0,0,[])
        print(res)
        result=[]
        for i in res:
            result.append(list(i))
        return result