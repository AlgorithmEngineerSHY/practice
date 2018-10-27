class Solution:
    def __init__(self):
        self.res = []

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        self.helper(n, 0, [], k)
        return self.res

    def helper(self, n, idx, path, k):
        if k == 0:
            self.res.append(path)

        if n - idx < k:
            return None

        for i in range(idx + 1, n + 1):
            self.helper(n, i, path + [i], k - 1)

obj = Solution()
print(obj.combine(4, 2))