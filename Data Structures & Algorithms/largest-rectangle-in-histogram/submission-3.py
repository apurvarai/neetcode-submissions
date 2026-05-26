class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        ans=float('-inf')
        for i in range(n):
            j=i-1
            while j>=0 and heights[j]>=heights[i]:
                j-=1
            left=j+1
            j=i+1
            while j<=n-1 and heights[j]>=heights[i]:
                j+=1
            right=j-1
            ans=max(ans,heights[i]*(right-left+1))
        return ans

        


        