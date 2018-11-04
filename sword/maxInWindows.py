
class Solution:
    def maxInWindows(self, num, size):
        if size <= 0:
            return []
        res = []
        for i in range(len(num) - size + 1):
            res.append(max(num[i: i + size]))
        return res