class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sum_a = sum(A)
        sum_b = sum(B)
        target = sum_a - (sum_a + sum_b) // 2
        set_b = set(B)
        res = []
        for i in A:
            if i - target in set_b:
                res.append(i)
                res.append(i - target)
                return res