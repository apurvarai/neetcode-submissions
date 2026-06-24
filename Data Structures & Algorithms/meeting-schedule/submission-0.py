"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        for i in range(1,len(intervals)):
            s=intervals[i].start
            e=intervals[i-1].end
            if e>s:
                return False
        return True
