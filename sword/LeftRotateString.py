class Solution:
    def LeftRotateString(self, s, n):
        if not s:
            return ''
        len_s = len(s)
        n = n % len_s
        return s[n:] + s[:n]
obj = Solution()
print(obj.LeftRotateString('2345', 2))