class Solution(object):
    def __init__(self):
        self.res = []

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) > 12:
            return []
        self.helper(s, 0, '')
        return self.res

    def helper(self, s, num, ip):
        if num == 4 and s =='':
            self.res.append(ip[1:])
            return
        for i in range(1, 4):
            if i <= len(s):

                if int(s[:i]) <= 255:
                    self.helper(s[i:], num + 1, ip + '.' + s[:i])
                if s[0] == '0':
                    break
