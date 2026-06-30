class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
       res=[]
       A,curr=[],[]
       count=defaultdict(int)

       #building A and count--> count helps to track freq,A is what we use in backtrack
       for num in candidates:
            if count[num]==0:
               A.append(num)
            count[num]=1+count.get(num,0)

       def dfs(A,i,target,curr):
            if target==0:
                # print(curr)
                res.append(curr.copy())
                return
            if target<0 or i==len(A):
                return
            if count[A[i]]>0:
                curr.append(A[i])
                count[A[i]]-=1
                dfs(A,i,target-A[i],curr)
                curr.pop()
                count[A[i]]+=1
            dfs(A,i+1,target,curr)
       dfs(A,0,target,curr)
       return res
