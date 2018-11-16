class Solution:
    def __init__(self):
        self.set_ = set()
        self.m = None

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        self.m = M
        res = 0
        for p in range(len(M)):
            if p not in self.set_:
                self.helper(p)
                res += 1
        return res

    def helper(self, p):
        for nei, is_friend in enumerate(self.m[p]):
            if is_friend and nei not in self.set_:
                self.set_.add(nei)
                self.helper(nei)


