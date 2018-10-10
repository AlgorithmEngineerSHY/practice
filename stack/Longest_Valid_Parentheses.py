'''
Given a string containing just the characters '(' and ')', 
find the length of the longest valid (well-formed) parentheses substring.
'''


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        if not s or len_s == 1:
            return 0
        datas = [(i, x) for i, x in enumerate(list(s))]
        stack = []
        for data in datas:
            if not stack:
                stack.append(data)
            else:
                tmp = stack.pop()
                if tmp[1] == '(' and data[1] == ')':
                    continue
                else:
                    stack.append(tmp)
                    stack.append(data)
        if not stack:
            return len_s

        else:
            max_len = 0
            tmp_len = stack[0][0]
            if max_len < tmp_len:
                max_len = tmp_len
            for i in range(len(stack) - 1):
                tmp_len = stack[i + 1][0] - stack[i][0] - 1
                if max_len < tmp_len:
                    max_len = tmp_len
            tmp_len = len_s - stack[-1][0] - 1
            if max_len < tmp_len:
                max_len = tmp_len
        return max_len
a=Solution()
b="())"
print(a.longestValidParentheses(b))