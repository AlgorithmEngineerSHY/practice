
class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        len_S = len(S)
        if len_S < 3:
            return []
        res = []
        mark = S[0]
        left = right = 0
        for idx in range(1, len_S):
            if mark == S[idx]:
                right += 1
            else:
                minus = right - left + 1
                if minus >= 3:
                    res.append([left, right])
                left = right = idx
                mark = S[idx]
        minus = right - left + 1
        if minus >= 3:
            res.append([left, right])
        return res