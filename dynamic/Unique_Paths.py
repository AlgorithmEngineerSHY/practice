class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        re = 1
        for i in range(n - 1):
            re *= (m + i) / (n - 1 - i)
        return round(re)

obj = Solution()
print(obj.uniquePaths(10,10))