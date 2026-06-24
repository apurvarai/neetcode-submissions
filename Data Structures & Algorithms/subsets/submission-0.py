class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        res.append([])
        def dfs(i,curr):
            
            if i==len(nums):
                # res.append(curr)
                return
            # res.append(curr.copy())
            curr.append(nums[i])
            res.append(curr.copy())
            # res.append(curr)
            dfs(i+1,curr)
            # res.append(curr.copy())
            curr.pop()
            dfs(i+1,curr)
        dfs(0,[])
        # print(set(res))
        # return set(res)
        return res
        