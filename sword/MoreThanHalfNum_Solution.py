from collections import Counter
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        ct = Counter(numbers)
        len_n_d2 = len(numbers) // 2 + 1
        for i in ct:
            if ct[i] >= len_n_d2:
                return i
        return 0

