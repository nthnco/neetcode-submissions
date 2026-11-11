"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        count = 0
        ans = 0
        intervals.sort(key=lambda i: i.start)
        starts = [i.start for i in intervals]
        ends = [i.end for i in intervals]
        s,e = 0,0
        while s != len(intervals):
            if starts[s] < ends[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            if count > 1:
                return False
        return True




