
from functools import cmp_to_key
class Solution:
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        list_n = [str(x) for x in range(1, n + 1)]
        list_n = sorted(list_n, key=cmp_to_key(self.sort))
        list_n = [int(x) for x in list_n]
        return list_n

    def sort(self, x, y):
        min_len = min(len(x), len(y))
        for i in range(min_len):
            if y > x:
                return -1
            elif y == x:
                continue
            else:
                return 1
        if len(x) == min_len:
            return -1
        else:
            return 1
