class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        s = s.split(' ')
        return '%20'.join(s)