
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        res = 0
        tmp = n
        base = 1
        while tmp:
            last = tmp % 10
            tmp = tmp // 10
            if last == 0:
                res += tmp * base
            elif last == 1:
                res += tmp * base
                res += n % base + 1
            else:
                res += (tmp + 1) * base
            base *= 10
        return res