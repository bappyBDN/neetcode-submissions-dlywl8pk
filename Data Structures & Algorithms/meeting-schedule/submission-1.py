"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        n=len(intervals)
        for i in range(n):
            A=intervals[i]
            for j in range(i+1,n):
                B=intervals[j]
                if A.end > B.start:
                    return  False
        return True
