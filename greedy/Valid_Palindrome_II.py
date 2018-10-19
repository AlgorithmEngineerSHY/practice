class Solution(object):

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        is_true, i, j = self.helper(s, 0, len(s) - 1)
        if is_true:
            return True
        else:
            is_true_1, i_1, j_1 = self.helper(s, i, j - 1)
            if is_true_1:
                return True
            is_true_2, i_2, j_2 = self.helper(s, i + 1, j)
            if is_true_2:
                return True
            return False

    def helper(self, q, i, j):
        while j > i:
            # print(i, j)
            if q[i] == q[j]:
                i += 1
                j -= 1
            else:
                return False, i, j
        return True, i, j