class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        i=0
        j=i+1
        ans=0
        while j<n:
            while j<n and prices[i]<=prices[j]:
                # j+=1
                ans=max(ans,prices[j]-prices[i])
                j+=1
            if j<n and prices[i]>prices[j]:
                i=j
                j=i+1
        return ans

        