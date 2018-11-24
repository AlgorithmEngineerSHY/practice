from itertools import groupby
class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = groupby(s)
        res = 0
        old_iter = None
        for key, group in s:
            if not old_iter:
                old_iter = list(group)
            else:
                new_iter = list(group)
                res += min(len(old_iter), len(new_iter))
                old_iter = new_iter
        return res