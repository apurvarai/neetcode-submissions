class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        i=0
        j=i+1
        ans=0
        for j in range(n):

            if prices[i]<prices[j]:
                ans=max(ans,prices[j]-prices[i])
                j+=1
            else:
                i=j
                j=i+1
        return ans
        