class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visit=set()
        res=set()
        n=len(nums)
        def dfs(subset):
            if len(subset)==n:
                print(subset)
                res.append(tuple(subset.copy()))
                return
            for i in range(n):
                if i in visit:
                    continue

                visit.add(i)
                subset.append(nums[i])
                dfs(subset)
                visit.remove(i)
                subset.pop()
                #//dfs(subset)
            
        dfs([])
        return res


        