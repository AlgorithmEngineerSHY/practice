class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if len(A) == 1:
            return 0
        min_num = min(A)
        max_num = max(A)
        min_num = min_num + K
        max_num = max_num - K
        if max_num > min_num:
            return max_num - min_num
        else:
            return 0