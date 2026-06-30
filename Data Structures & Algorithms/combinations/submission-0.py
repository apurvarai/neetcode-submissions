class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums,res=[],[]
        for i in range(1,n+1):
            nums.append(i)
        def dfs(i,cnt,subset):
            if cnt==k:
                res.append(subset.copy())
                return
            if cnt>k or i>=n:
                return
            cnt+=1
            subset.append(nums[i])
            dfs(i+1,cnt,subset)
            cnt-=1
            subset.pop()
            dfs(i+1,cnt,subset)
        dfs(0,0,[])
        return res
        