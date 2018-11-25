# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

from functools import cmp_to_key

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        sorted_intervals = sorted(intervals, key=cmp_to_key(self.sort_intervals))
        res = 0
        stack = []
        for i in range(len(sorted_intervals)):
            if not stack:
                stack.append(sorted_intervals[i])
            else:
                if stack[-1].end > sorted_intervals[i].start:
                    res += 1
                else:
                    stack.append(sorted_intervals[i])
        return res



    def sort_intervals(self, x, y):
        if y.end != x.end:
            return x.end - y.end
        else:
            return x.start - y.start