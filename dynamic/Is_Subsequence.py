class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        idx = 0
        len_s = len(s)
        for i in t:
            if i == s[idx]:
                idx += 1
                if idx == len_s:
                    return True
        return False