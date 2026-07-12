class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=set()
        res=[]
        n=len(nums)
        for i in range(n):
            #find nums[j]+nums[k]==-nums[i]
            j=i+1
            k=n-1
            while j<k:
                if nums[k]+nums[j]==-nums[i]:
                    ans.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif nums[k]+nums[j]>-nums[i]:
                    k-=1
                else:
                    j+=1
        print(ans)
        for i in ans:
            res.append(list(i))
        return res

        