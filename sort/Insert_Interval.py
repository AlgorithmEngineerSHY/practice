'''
Given a set of non-overlapping intervals, 
insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.
'''


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        s = newInterval.start
        e = newInterval.end
        left, right = [], []
        for interval in intervals:
            if interval.end < s:
                left.append(interval)
            elif interval.start > e:
                right.append(interval)
            else:
                s = min(s, interval.start)
                e = max(e, interval.end)
        return left + [Interval(s, e)] + right