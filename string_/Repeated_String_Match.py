class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        q = (len(B) - 1) // len(A) + 1
        for i in range(2):
            if B in A * (q + i):
                return q + i
        return -1