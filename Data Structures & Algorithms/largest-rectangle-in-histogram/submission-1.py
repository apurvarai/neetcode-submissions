class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        ans=max(heights)
        for i in range(2,n):
            #find min of consecutive i's and multiply it by i to get area
            ##to find min of cons. i's, create window of i's
            ##keep on updating window len(i)
            #compare with max and update
            p=0
            q=i-1
            #start with window of length i, from 0 index
            while q<=n-1:
                curr=i*(min(heights[p:q+1]))
                p+=1
                q+=1
                ans=max(curr,ans)
                # print(curr," ",i)
        return ans


        