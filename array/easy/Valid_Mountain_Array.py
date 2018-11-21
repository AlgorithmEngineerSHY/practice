class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        len_A = len(A)
        if len_A < 3:
            return False
        max_num = A[0]
        mark = 1
        for i in range(1, len_A):
            if A[i] > max_num and mark == 1:
                max_num = A[i]
            elif A[i] == max_num:
                return False
            elif mark == 1 and A[i] < max_num:
                mark = -1
            elif mark == -1 and A[i] < A[i - 1]:
                continue
            else:
                return False
        if mark == 1:
            return False
        elif max_num == A[0]:
            return False
        else:
            return True
