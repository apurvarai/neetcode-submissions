class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        cnt=0
        n=len(intervals)
        intervals.sort(key= lambda i:i[0])
        prevend=intervals[0][1]
        for i in range(1,n):
            if prevend<=intervals[i][0]:
                prevend=intervals[i][1]
            else:
                cnt+=1
                prevend=min(prevend,intervals[i][1])
        return cnt

        