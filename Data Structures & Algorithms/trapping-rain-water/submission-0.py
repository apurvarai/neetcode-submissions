class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left=[height[0]]*n
        right=[height[n-1]]*n
        res=0
        for i in range(1,len(height)):
            left[i]=max(left[i-1],height[i])
        for j in range(n-2,-1,-1):
            right[j]=max(right[j+1],height[j])
        for i in range(n):
            res+=(min(left[i],right[i])-height[i])

        return res

        