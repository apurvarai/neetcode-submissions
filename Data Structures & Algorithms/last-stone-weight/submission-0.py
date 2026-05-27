class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # stones.sort()
        while len(stones)>1:
            stones.sort()
            x=stones[len(stones)-1]
            y=stones[len(stones)-2]
            if x==y:
                stones.pop()
                stones.pop()
            else:
                stones.pop()
                stones.pop()
                stones.append(x-y)
        if len(stones)==1:
            return stones[0]
        else:
            return 0
        