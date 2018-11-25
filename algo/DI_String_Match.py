class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = [0] * (len(S) + 1)
        len_S = len(S)
        # n_I = S.count('I')
        # n_D = len_S - n_I
        max_num = len_S
        min_num = 0
        for i, s in enumerate(S):
            if s == 'I':
                res[i] = min_num
                min_num += 1
            else:
                res[i] = max_num
                max_num -= 1
        res[-1] = max_num
        return res