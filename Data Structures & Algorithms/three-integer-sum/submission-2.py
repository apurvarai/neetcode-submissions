class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        nums.sort()
        res=set()
        for k in range(n):
            target=-nums[k]
            i=0
            j=n-1
            while i<j:
                if i==k or j==k:
                    if i==k:
                        i+=1
                    if j==k:
                        j-=1
                    continue
                else:
                    if nums[i]+nums[j]==target:
                        res.add(tuple(sorted([nums[i],nums[j],nums[k]])))
                        i+=1
                        j-=1
                        # return [nums[i],nums[j],nums[k]]
                    elif nums[i]+nums[j]>target:
                        j-=1
                    else:
                        i+=1
        print(res)
        return list(res) 

        