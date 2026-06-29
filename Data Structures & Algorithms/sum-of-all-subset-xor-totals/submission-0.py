class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res=[]
        n=len(nums)
        def dfs(i,subset):
            if i==n:
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1,subset)
            subset.pop()
            dfs(i+1,subset)
            # return
        dfs(0,[])
        print(res)
        sum=0
        for l in res:
            s=0
            for i in l:
                s^=i
            sum+=s
        return sum

        