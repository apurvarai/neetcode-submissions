class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0]) #sort wrt start time
        curr=intervals[0]
        res=[]
        for i in range(1,len(intervals)):
            if curr[1]<intervals[i][0]:
            # add curr to res
                res.append(curr.copy())
                curr=intervals[i]
            else:
                curr=[curr[0],max(curr[1],intervals[i][1])]
        res.append(curr)
        return res

        