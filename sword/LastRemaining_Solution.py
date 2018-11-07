
class Solution:
    def LastRemaining_Solution(self, n, m):
        if m == 0 or n == 0:
            return -1
        n_list = [x for x in range(n)]
        idx = 0
        while n > 1:
            idx = (m + idx - 1) % n
            n_list.pop(idx)
            n -= 1
        return n_list[0]
obj = Solution()
print(obj.LastRemaining_Solution(5, 3))