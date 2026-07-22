class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good=set()
        for i in triplets:
            if i[0]>target[0]:
                continue
            if i[1]>target[1]:
                continue
            if i[2]>target[2]:
                continue
            for x,y in enumerate(i):
                print(x,y)
                if y>=target[x]:
                    good.add(x)
        if 0 in good and 1 in good and 2 in good:
            return True
        return False