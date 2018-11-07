
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        len_s = len(s)
        len_p = len(pattern)
        if len_s == 0 and len_p == 0:
            return True
        if len_s > 0 and len_p == 0:
            return False
        if len_p > 1 and pattern[1] == '*':
            if len_s > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
                return self.match(s, pattern[2:]) or self.match(s[1:], pattern[2:]) or self.match(s[1:], pattern)
            else:
                return self.match(s, pattern[2:])
        if len_s > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
            return self.match(s[1:], pattern[1:])
        return False