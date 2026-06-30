class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=set()
        n=len(nums)
        def dfs(i,subset):
            if i==n:
                res.add(tuple(sorted(subset)))
                return
            subset.append(nums[i])
            dfs(i+1,subset)
            subset.pop()
            dfs(i+1,subset)
        dfs(0,[])
        # print(res)
        # for i in res:
        #     result.append(list(i)
        result=[list(i) for i in res]
        return result

        

        