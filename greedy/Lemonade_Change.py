from collections import Counter
class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if not bills:
            return True
        c = Counter()
        for b in bills:
            if b == 5:
                c[5] += 1
            elif b == 10:
                if c[5] == 0:
                    return False
                else:
                    c[5] -= 1
                    c[10] += 1
            else:
                if c[10] > 0:
                    if c[5] > 0:
                        c[5] -= 1
                        c[10] -= 1
                        continue
                if c[5] < 3:
                    return False
                else:
                    c[5] -= 3
        return True






