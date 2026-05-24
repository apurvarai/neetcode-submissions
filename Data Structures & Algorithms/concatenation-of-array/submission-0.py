class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # l=[]
        nums.extend(nums)
        # print(l)
        return nums
        