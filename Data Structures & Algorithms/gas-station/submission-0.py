class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ans=-1
        for i in range(len(gas)):
            newgas=gas[i:]+gas[:i]
            newcost=cost[i:]+cost[:i]
            curr=gas[i]
            for j in range(len(newgas)):
                if j<(len(newgas)-1) and curr>=newcost[j]:
                    curr+=(newgas[j+1]-newcost[j])
                else:
                    curr-=newcost[j]
                if curr<=0:
                    break
                print(i," ",j," ",curr)
                if curr>0 and j==len(newgas)-1:
                    ans=i
                    return ans
                print(i," ",j," ",curr)
        return ans 
        