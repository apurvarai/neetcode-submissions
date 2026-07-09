class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if n%groupSize:
            return False
        hand.sort()
        count=Counter(hand)
        for num in hand:
            if count[num]:
                for i in range(num,num+groupSize):
                    if not count[i]:
                        return False
                    count[i]-=1
            # if j>=n or len(res)>=groupSize:
        return True



            # for j in range(i+1,groupSize+i-1):


        