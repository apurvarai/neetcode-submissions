class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #for each pos, count how many earlier pos have
        #prefix sum equal to currprefix-k
        #how many earlier [prefixsums were prefix[r]-k]
        mp={0:1}
        cnt,curr=0,0
        for i in nums:
            curr+=i
            cnt+=mp.get(curr-k,0)
            mp[curr]=1+mp.get(curr,0)
        return cnt

        
        