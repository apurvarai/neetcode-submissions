class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0])
        curr=intervals[0]
        res=[]
        # new=intervals[1]
        res.append(curr.copy())
        for new in intervals[1:]:
            if new[0]>curr[1]:
                res.append(new.copy())
            else:
                new[0]=min(new[0],curr[0])
                new[1]=max(new[1],curr[1])
                res.pop()
                res.append(new.copy())
                print(new)
            curr=res[-1]

        return res
        