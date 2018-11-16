class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        # map_dict = {'0': '0', '1': '1', '8': '8', '2': '5', '5': '2', '6': '9', '9': '6'}
        for num in range(1, N + 1):
            num = str(num)
            if '3' in num or '4' in num or '7' in num:
                continue
            if '2' in num or '5' in num or '6' in num or '9' in num:
                res += 1
        return res



