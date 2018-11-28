class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''
        stack = [s[0]]

        for i in s[1:]:
            if i != ']':
                stack.append(i)
            else:
                tmp_string = ''
                while stack[-1] != '[':
                    tmp_string = stack.pop() + tmp_string
                stack.pop()
                tmp_num = ''
                while stack and stack[-1].isnumeric():
                    tmp_num = stack.pop() + tmp_num
                stack.append(tmp_string * int(tmp_num))
        return ''.join(stack)
