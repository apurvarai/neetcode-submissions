class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        nums=prices
        for i in range(len(prices)-1):
            if nums[i]<nums[i+1]:
                profit+=(nums[i+1]-nums[i])
        return profit