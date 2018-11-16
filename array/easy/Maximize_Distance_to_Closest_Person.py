from itertools import groupby
class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        res = 0
        for seat, group in groupby(seats):
            if not seat:
                res = max(res, (len(list(group)) + 1) // 2)
        return max(res, seats.index(1), seats[::-1].index(1))





