class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        docs = [x for x in path.split('/') if x != '.' and x != '']
        res = []
        for i in docs:
            if i == '..':
                if res:
                    res.pop()
            else:
                res.append(i)
        re = '/' + '/'.join(res)
        return re

obj = Solution()
print(obj.simplifyPath("/a//b////c/d//././/.."))