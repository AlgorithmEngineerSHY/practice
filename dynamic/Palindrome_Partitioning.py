class Solution:
    def __init__(self):
        self.re = []
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.dfs(s, [])
        return self.re

    def dfs(self, s, re_tmp):
        if not s:
            self.re.append(re_tmp)

        for i in range(1, len(s) + 1):
            if self.is_pal(s[:i]):
                self.dfs(s[i:], re_tmp + [s[:i]])

    def is_pal(self, s):
        return s == s[::-1]