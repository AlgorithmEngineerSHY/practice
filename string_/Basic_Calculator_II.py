class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(' ', '')
        S = []
        tmp = ''
        for i in s:
            if i.isnumeric():
                tmp += i
            else:
                S.append(int(tmp))
                tmp = ''
                S.append(i)
        S.append(int(tmp))
        stack = []
        for i in S:
            if not stack:
                stack.append(i)
            elif stack[-1] == '*':
                stack.pop()
                stack.append(stack.pop() * i)
            elif stack[-1] == '/':
                stack.pop()
                stack.append(stack.pop() // i)
            else:
                stack.append(i)
        res = 0
        mark = 1
        for i in stack:
            if i == '+':
                mark = 1
            elif i == '-':
                mark = -1
            else:
                res += i * mark
        return res
obj = Solution()
print(obj.calculate("3+2*2"))


