n = int(input())
power_val = [int(x) for x in input().split(' ')]
tmp = [int(x) for x in input().split(' ')]
k, d = tmp[0], tmp[1]

class Solution:
    def __init__(self, n, power_val, k, d):
        self.n = n
        self.power_val = power_val
        self.k = k
        self.d = d
        self.res = -float('inf')

    def he_chang_tuan(self):
        self.helper(-1, self.k, 1)
        return self.res

    def helper(self, idx, tmp_k, pro):
        if tmp_k == 0:
            self.res = max(self.res, pro)
        if self.n - idx - 1 < tmp_k:
            return None
        for i in range(idx + 1, idx + self.d + 1):
            if i < self.n:
                self.helper(i, tmp_k - 1, pro * self.power_val[i])

obj = Solution(n, power_val, k, d)
print(obj.he_chang_tuan())