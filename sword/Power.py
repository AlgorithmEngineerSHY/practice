class Solution:
    def Power(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        if exponent < 0:
            exponent = -exponent
            base = 1 / base
        return self.helper(base, exponent)

    def helper(self, base, exponent):
        if exponent == 1:
            return base

        if exponent % 2 == 0:

            return self.Power(base ** 2, exponent // 2)
        else:
            return base * self.Power(base, exponent - 1)
obj = Solution()
print(obj.Power(2, -3))