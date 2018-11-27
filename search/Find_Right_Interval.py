# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def __init__(self):
        self.start_idx = None


    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        start_idx = [(x.start, idx) for idx, x in enumerate(intervals)]
        start_idx = sorted(start_idx, key=lambda x: x[0])
        self.start_idx = start_idx
        res = []
        for idx, interval in enumerate(intervals):
            if interval.end > start_idx[-1][0]:
                res.append(-1)
            else:

                res.append(self.binary_search(0, len(intervals) - 1, interval.end))
        return res

    def binary_search(self, left, right, target):

        mid = (left + right) // 2
        if self.start_idx[mid][0] == target:
            return self.start_idx[mid][1]
        elif self.start_idx[mid][0] > target:
            right = mid - 1

        else:
            left = mid + 1

        if right > left:
            return self.binary_search(left, right, target)
        else:
            tmp_list = []
            for i in range(left - 1, left + 2):
                if i < len(self.start_idx) and self.start_idx[i][0] >= target:
                    tmp_list.append(self.start_idx[i][1])
            return min(tmp_list)

obj = Solution()
print(obj.findRightInterval([Interval(3,4),Interval(2,3),Interval(1,2)]))