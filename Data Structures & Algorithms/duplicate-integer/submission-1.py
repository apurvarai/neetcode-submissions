class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp={}
        for i,val in enumerate(nums):
            if val in mp:
                return True
            mp[val]=i
        return False
        