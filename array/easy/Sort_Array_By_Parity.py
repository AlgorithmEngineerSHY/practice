from collections import deque
class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        q = deque()
        helper = [x % 2 == 0 for x in A]
        for idx, is_even in enumerate(helper):
            if is_even:
                q.appendleft(A[idx])
            else:
                q.append(A[idx])
        return list(q)