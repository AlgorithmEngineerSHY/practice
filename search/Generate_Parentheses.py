class Solution:
    def __init__(self):
        self.res = []
        self.n = None
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.n = n
        self.helper('', 0, 0)
        return self.res


    def helper(self, s, left, right):
        if len(s) == 2 * self.n:
            self.res.append(s)
            return None
        if left < self.n:
            self.helper(s + '(', left + 1, right)
        if right < left:
            self.helper(s + ')', left, right + 1)

