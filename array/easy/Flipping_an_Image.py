class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        for A_row in A:
            res.append([1 if x == 0 else 0 for x in reversed(A_row)])
        return res