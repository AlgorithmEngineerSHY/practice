class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return None
        if n == 1:
            return 1
        res = [1]
        idx_2 = idx_3 = idx_5 = 0
        for i in range(1, n):
            n2 = res[idx_2] * 2
            n3 = res[idx_3] * 3
            n5 = res[idx_5] * 5
            nx = min(n2, n3, n5)
            res.append(nx)
            if n2 == nx:
                idx_2 += 1
            if n3 == nx:
                idx_3 += 1
            if n5 == nx:
                idx_5 += 1
        return res[-1]
