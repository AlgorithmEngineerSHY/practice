class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res = []
        mark = -float('inf')
        for idx, alpha in enumerate(S):
            if alpha == C:
                res.append(0)
                mark = idx
            else:
                res.append(idx - mark)
        re_res = []
        mark = -float('inf')
        for idx, alpha in enumerate(S[::-1]):
            if alpha == C:
                re_res.append(0)
                mark = idx
            else:
                re_res.append(idx - mark)
        re_res = list(reversed(re_res))
        return [min(x) for x in zip(res, re_res)]