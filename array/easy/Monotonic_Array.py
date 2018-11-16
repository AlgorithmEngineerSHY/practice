class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if not A:
            return False
        if len(A) == 1:
            return True
        big = lambda x, y: x >= y
        small = lambda x, y: x <= y
        if A[-1] - A[0] >= 0:
            func = small
        else:
            func = big
        for idx in range(len(A) - 1):
            if func(A[idx], A[idx + 1]):
                continue
            else:
                return False
        return True

