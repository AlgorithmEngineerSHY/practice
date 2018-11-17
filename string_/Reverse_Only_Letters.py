class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        ss = [x for x in S if x.isalpha()]
        res = ''
        for s in S:
            if s.isalpha():
                res += ss.pop()
            else:
                res += s
        return res
