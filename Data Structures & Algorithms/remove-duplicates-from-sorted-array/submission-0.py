class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(len(nums)-1):
            if i+1>len(nums)-1:
                break
            if nums[i]==nums[i+1]:
                nums.pop(i+1)
                continue

        return len(nums)
        