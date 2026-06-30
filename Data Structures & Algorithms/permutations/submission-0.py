class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        visit=set()
        def dfs(subset):
            if len(subset)==n:
                res.append(subset.copy())
                return
            for num in nums:
                if num in visit:
                    continue
                subset.append(num)
                visit.add(num)
                dfs(subset)
                visit.remove(num)
                subset.pop()
        dfs([])
        return res
        