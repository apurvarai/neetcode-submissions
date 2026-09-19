class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        i=0
        j=1
        profit=0
        ans=0
        while j<n:
            if prices[i]<=prices[j]:
                profit=prices[j]-prices[i]
                ans=max(ans,profit)
                j=j+1
            else:
                i=j
                j=i+1
        return ans
        