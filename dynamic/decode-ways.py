class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        first, second, pre = 0, int(s > ''), ''
        for i in s:
            first, second, pre = second, second * (int(i) > 0) + first * (9 < int(pre + i) < 27), i
        return second

obj = Solution()
print(obj.numDecodings('226'))
